#include "../headers/common.h"

int addition(){

    while (true) {

        string a, b;
        double c, d;

        cout << "Enter two numbers below:\n";

        // Asks for input and tries converting string to double or int.
        // If conversion fails in any of the two nested try statements, enter a failed conversion state and re-loop.

        cin >> a;
        try{
            c = stod(a);
        } catch (invalid_argument&) {
            try {
                c = stoi(a);
        } catch (invalid_argument&) {
            cout << "Could not convert first" << endl;
            continue;
            }
        }

        cin >> b;
        try{
            d = stod(b);
        } catch (invalid_argument&) {
            try {
                d = stoi(b);
        } catch (invalid_argument&) {
            cout << "Could not convert second" << endl;
            continue;
            }
        }

        // Figure out whether the result is integer or double.
        // It creates a stringsteam object, adds the result of c+d to the sstream, and check if the result contains any dots.

        stringstream ss;
        ss << c+d;
        string result = ss.str();

        bool isDec = false;
        for (char digit : result){
            if (digit == '.') {
                isDec = true;
                break;
            }
        }

        // Print the result to the console depending on the number

        int ans_int;
        double ans_dub;
        string ofType;

        if (!isDec)
        {
            ans_int = stoi(result);
            ofType = " of type Integer";
            cout << c << " + " << d << " = " << ans_int << ofType << endl;
            cout << typeid(ans_int).name() << endl;
        }
        else
        {
            ans_dub = stod(result);
            ofType = " of type Double";
            cout << c << " + " << d << " = " << ans_int << ofType << endl;
            cout << typeid(ans_dub).name() << endl;
        }

        // Continue?
        string cnt;
        cout << "Again?" << endl;
        cin >> cnt;

        // If first letter and second letter of cnt, in lowercase, are 'n' and 'o' respectively, exit
        // Else, continue
        // Uses "" for string on string type matching.
        if (string(1, tolower(cnt[0])) == "n" && string(1, tolower(cnt[1])) == "o") {
            cout << "Ending..";
            break;
        } else { continue; }


    } // End of while loop

    return 0;

} // End of function
