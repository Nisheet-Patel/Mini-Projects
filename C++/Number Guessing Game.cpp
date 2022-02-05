#include <iostream>
#include<stdlib.h>
#include<cstdlib>
#include<ctime>
#include<cctype>    
using namespace std;


// Global Variables
int bot_guess;

// Genrate Random number
void genrate_guess(int i){
    cout << "\nI Guess Number Between 1 to " << i << endl;
    bot_guess = 1 + (rand() % i);
}

void Title(){
    // Title
    cout << "  ____                     _                ____                      "<< endl;
    cout << " / ___|_   _  ___  ___ ___(_)_ __   __ _   / ___| __ _ _ __ ___   ___ "<< endl;
    cout << "| |  _| | | |/ _ \\/ __/ __| | '_ \\ / _` | | |  _ / _` | '_ ` _ \\ / _ \\ "<< endl;
    cout << "| |_| | |_| |  __/\\__ \\__ \\ | | | | (_| | | |_| | (_| | | | | | |  __/"<< endl;
    cout << " \\____|\\__,_|\\___||___/___/_|_| |_|\\__, |  \\____|\\__,_|_| |_| |_|\\___|"<< endl;
    cout << "                                   |___/                              "<< endl;  
}

int main()
{
    srand(time(0)); // Truly random Numbers
    int difficulty, user_guess, attemps = 0;
    char play;

    // Choosing Difficulty of Game
    do{
    system("cls");
    Title();            // Title
    cout << "\nNote: You have maximum 10 attempts to guess my number.\n" << endl;
    cout << "Choose Game Difficulty: " << endl;
    cout << "1> Easy\n2> Medium\n3> Hard\n:";
    cin >> difficulty;

    if(difficulty==1)
        genrate_guess(10);
    else if (difficulty==2)
        genrate_guess(50);
    else if (difficulty==3)
        genrate_guess(100);
    else{
        cout << "plz Enter Number 1,2, or 3";
        _sleep(2000);
    }    
    }while(difficulty>=4);


    // Algorithm
    do{
        if(attemps > 10){   // Attemps more than 10 stops game
            cout << "\n:( You Loss The Game ...";
            break;
        }

        cout << ":";        
        cin >> user_guess;

        if(user_guess<bot_guess){
            cout << "Higher number please!" << endl;
            attemps += 1;
        }
        else if(user_guess>bot_guess){
            cout << "Lower number please!" << endl;
            attemps += 1;
        }
        else{
            printf("\n:) You guessed the number in %d attempts\n",attemps);
        }
        
    }while(user_guess!=bot_guess);
    

    // If player Wants to play again
    cout << "\nDo You want to play Again\n[y|n]:";
    cin >> play;
    if(tolower(play)=='y'){
        system("cls");
        main();
    }
    else{
        system("cls");
    }
    return 0;
}

