#include <iostream>
#include <cctype> // std::tolower, std::isdigit
#include <algorithm> // std::transform, std::find, std::distance
#include <map>
#include <array>
#include <vector>
// #include <iterator> // std::begin (constexpr)
#include <chrono> // std::chrono::milliseconds
#include <thread> // std::this_thread::sleep_for
#include <random>


// remnant of constexpr but c++14
std::array<std::pair<int, int>, 9> generate_moves()
{
    std::array<std::pair<int, int>, 9> moves;
    auto it = std::begin(moves);
    
    for (int r = 0; r < 3; r++)
    for (int c = 0; c < 3; c++)
    {
        it->first = r;
        it->second = c;
        ++it;
    }

    /*     
    for (auto& pair : moves)
        std::cout << '{' << pair.first << ',' << pair.second << "}\n";
    std::cout << "~~~\n";
    */

    return moves;  
};

const auto all_moves = generate_moves();


int random(int min, int max)
{
    // most vexing parse
    static std::mt19937 gen((std::random_device())());
    std::uniform_int_distribution<> dist(min, max);
    return dist(gen);
}


std::pair<int, int>random_turn (std::vector<std::pair<int, int>>& moves_left)
{    
    std::random_device r;
    std::mt19937 gen(r());
    std::uniform_int_distribution<> dist(0, moves_left.size()-1);
    
    int i = dist(gen);
    std::pair<int, int> turn = moves_left[i];
    
    moves_left.erase(moves_left.begin() + i);
    
    return turn;
}


const std::array<std::string, 5> tile =
{
    "+---------+",
    "|         |",
    "|         |",
    "|         |",
    "+---------+"
};

const std::array<std::string, 5> nought =
{
    "+---------+",
    "|  OOOOO  |",
    "| O     O |",
    "|  OOOOO  |",
    "+---------+"
};

const std::array<std::string, 5> cross =
{
    "+---------+",
    "| XX   XX |",
    "|   XXX   |",
    "| XX   XX |",
    "+---------+"
};


class Game
{
    private:
        static std::map<char, std::array<std::string, 5>> tile_mapping;
        
        char game_board[3][3];
        int mode;
        
        std::vector<std::pair<int, int>> moves_left;
        
        std::string player1;
        char player1_icon;
        
        std::string player2;
        char player2_icon;
        
        int now_playing;
        int turn_counter;
        
        void (Game::*player1_turn)();
        void (Game::*player2_turn)();
        
    public:
        Game(int mode) : mode(mode)
        {
            prepare_game();
            default_board();
        }
        
        void prepare_game()
        {
            turn_counter = 0;
            
            moves_left = std::vector<std::pair<int, int>>(all_moves.begin(), all_moves.end());

            int first_player = random(0, 1);
            //std::cout << first_player << ' ' << (first_player ? "true" : "false") << '\n';
            
            player1_icon = first_player ? 'n' : 'c';
            player2_icon = (player1_icon == 'n') ? 'c' : 'n';
            //std::cout << player1_icon << ' ' << player2_icon << '\n';
            
            now_playing = first_player ? 1 : 2;
            
            if (mode == 0) // CPU
            {
                player1 = "You";
                player2 = "CPU";
                
                player1_turn = &Game::player_turn;
                player2_turn = &Game::cpu_turn;
                
                std::cout << "\nYou are " << (player1_icon == 'n' ? "Noughts" : "Crosses") << " and the CPU is " << (player2_icon == 'n' ? "Noughts" : "Crosses") << ".\n";
            }
            
            else // (mode == 1) // VS 
            {
                player1 = "P1";
                player2 = "P2";
                
                player1_turn = &Game::player_turn;
                player2_turn = &Game::player_turn;
                
                std::cout << "\nP1 is " << (player1_icon == 'n' ? "Noughts" : "Crosses") << " and P2 is " << (player2_icon == 'n' ? "Noughts" : "Crosses") << ".\n";
            }
            
            if (now_playing == 1)
                std::cout << player1 << (mode == 0 ? " are" : " is") << " first.\n\n";
            else // (now_playing == 2)
                std::cout << player2 << " is first.\n\n";
            
            std::cout << std::endl;
        }
        
        void default_board()
        {
            for (int row = 0; row < 3; row++)
            for (int col = 0; col < 3; col++)
                this->game_board[row][col] = 't';
        }
        
        bool full_board()
        {
            return (turn_counter >= 9);
        }
        
        void print_board()
        {
            for (int row = 0; row < 3; row++)
            {
                std::array<std::string, 5> display_row = {"", "", "", "", ""};
                
                for (int col = 0; col < 3; col++)
                {
                    auto& str_row = this->tile_mapping[game_board[row][col]];
                    
                    display_row[0] += str_row[0] + ' ';
                    display_row[1] += str_row[1] + ' ';
                    display_row[2] += str_row[2] + ' ';
                    display_row[3] += str_row[3] + ' ';
                    display_row[4] += str_row[4] + ' ';
                }
                    
                for (auto& sub_row : display_row)
                    std::cout << sub_row << '\n';
                std::cout << std::endl;
            }
        }
        
        void print_turn()
        {
            if (now_playing == 1)
                std::cout << '[' << player1 << ']';
            else // (now_playing == 2)
                std::cout << '[' << player2 << ']';
            
            std::cout << std::endl;
        }
        
        void play()
        {
            if (now_playing == 1)
                (this->*player1_turn)();
            
            else // (now_playing == 2)
                (this->*player2_turn)();
                
            turn_counter += 1;
            now_playing = (now_playing == 1) ? 2 : 1;
        }
        
        void player_turn()
        {
            while (true)
            {
                std::cout << ": ";
                std::string input;
                std::getline(std::cin, input);
                std::cout << std::endl;
                
                // *
                auto turn = is_valid_turn(input);
          
                if (not std::get<0>(turn))
                {
                    std::cout << "Try again\n";
                    continue;
                }
                
                int r = std::get<1>(turn);
                int c = std::get<2>(turn);
                
                this->game_board[r][c] = (now_playing == 1) ? player1_icon : player2_icon;
                moves_left.erase(std::find(moves_left.begin(), moves_left.end(), std::make_pair(r, c)));
                
                break;
            }
        }
        
        // *  consider changing function to use moves_left instead
        std::tuple<bool, int, int> is_valid_turn(std::string move)
        {
            if (move.size() != 3 or move[1] != ',')
                return std::make_tuple(0, 0, 0);
            
            if (not std::isdigit(move[0]) or not std::isdigit(move[2]))
                return std::make_tuple(0, 0, 0);

            int r = (move[0] - '0') - 1;
            int c = (move[2] - '0') - 1;
            
            if (r < 0 or r > 2 or c < 0 or c > 2)
                return std::make_tuple(0, 0, 0);
            
            if (this->game_board[r][c] != 't')
                return std::make_tuple(0, 0, 0);
            
            return std::make_tuple(true, r, c);
        }
        
        void cpu_turn()
        {
            auto turn = random_turn(moves_left);
            int r = std::get<0>(turn);
            int c = std::get<1>(turn);
             
            //std::cout << "\n(" << r+1 << ',' << c+1 << ")\n";
            
            this->game_board[r][c] = player2_icon;
            std::this_thread::sleep_for(std::chrono::milliseconds(1000));
        }
        
        bool win()
        {
            // rows
            for (int row = 0; row < 3; row++)
            {
                char p = game_board[row][0];
                
                if (p == 't')
                    continue;
                    
                int c = 0;
                for (int col = 1; col < 3; col++)
                {
                    if (game_board[row][col] == p)
                        c++;
                }
                if (c == 2)
                    return true;
            }
            
            // columns
            for (int col = 0; col < 3; col++)
            {
                char p = game_board[0][col];
                
                if (p == 't')
                    continue;
                    
                int c = 0;
                for (int row = 1; row < 3; row++)
                {
                    if (game_board[row][col] == p)
                        c++;
                }
                if (c == 2)
                    return true;
            }
            
            // diagonal top-left/bottom-right
            char sq = game_board[0][0];
            if (sq == 't'){}
            else if (game_board[1][1] == sq and game_board[2][2] == sq)
                return true;
            
            // diagonal top-right/bottom-left
            sq = game_board[0][2];
            if (sq == 't'){}
            else if (game_board[1][1] == sq and game_board[2][0] == sq)
                return true;
            
            return false;
        }
        
        void end_game()
        {
            // last phase of the game Game::play() already swapped now_playing
            std::cout << (now_playing == 1 ? this->player2 : this->player1) << " won!\n";
        }
        
};

std::map<char, std::array<std::string, 5>> Game::tile_mapping = 
{
    {'t', tile},
    {'n', nought},
    {'c', cross}
};


int main(void)
{
    std::cout << __cplusplus << '\n';

    std::cout << "Noughts & Crosses\n\n";
    
    std::cout << "[CPU] :: [VS]\n";
        
    int mode;
    while (true)
    {
        std::string input;
        std::cout << ": ";
        std::getline(std::cin, input);
        
        std::transform(input.begin(), input.end(), input.begin(), [](unsigned char c){ return std::tolower(c); });
        
        if (input == "cpu")
            mode = 0;
        else if (input == "vs")
            mode = 1;
        else
            continue;
        
        std::cout << std::endl;
        
        break;
    }
    
    Game game(mode);
    
    
    while (true)
    {
        game.print_board();
        game.print_turn();
        
        //break;
        
        game.play();
        
        if (game.win())
        {
            game.print_board();
            game.end_game();
            break;
        }
        
        else if (game.full_board())
        {
            game.print_board();
            std::cout << "\nIt's a draw!\n";
            break;
        }

    }
    
    return 0;
}





