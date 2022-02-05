/*
Rock Paper Sicssor Game
- Ascii Art Hands
- Default Rounds 4
- Computer Player

Creator : Nisheet Patel
Github  : https://github.com/NisheetNakrani
*/
#include <iostream>
#include <conio.h>
#include <map>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;

// Change game rounds
#define ROUND 4

class Player
{
private:
    map<int, char> nchoice = {{1, 'R'}, {2, 'P'}, {3, 'S'}};

public:
    char option;
    string Name;
    int score = 0;

    // Update Name
    Player(string name) : Name(name){};

    // Update User Input Choice
    void choice(int i)
    {
        option = nchoice.at(i);
    }

    // Check if this->Player wins
    int iswin(Player &P)
    {
        // true = 1, false = 0, tie = 2
        if (option == P.option)
            return 2;
        if (option == 'R' && P.option == 'S')
            return 1;
        else if (option == 'P' && P.option == 'R')
            return 1;
        else if (option == 'S' && P.option == 'P')
            return 1;
        return 0;
    }

    // return Random number 1,2,3
    int rand_choice()
    {
        srand(time(0));
        return 1 + rand() % 3;
    }

    // increment score
    void update_score()
    {
        score++;
    }
};

void Logo();
void show_hand(int, int);
void display(string, string, int, int, int, int, int);

int main()
{
    /*
    | p1h = User Choice
    | p2h = Computer Choice
    |
    '-> Use for show_hand();
    
    */
    int User, win, p1h = 0, p2h = 0, round = 1;
    string name, YN;

    // Get Name
    cout << "Enter Name : ";
    cin >> name;

    // Two Players
    Player p1(name), p2("Computer");

    // Total 4 Rounds
    while (round <= ROUND)
    {

        display(p1.Name, p2.Name, round, p1h, p2h, p1.score, p2.score);

        // input guide
        cout << "[ 1 ] Rock -- [ 2 ] Paper - [ 3 ] Sicssor\n?";

        try
        {
            cin >> User; // User Input

            if (User > 3)
                throw(400);

            p1h = User;
            p1.choice(User); // User Choice

            p2h = p2.rand_choice();
            p2.choice(p2h); // Computer Choice

            win = p1.iswin(p2);

            display(p1.Name, p2.Name, round, p1h, p2h, p1.score, p2.score);

            // print current choice
            printf("Status : %c - %c\n", p1.option, p2.option);

            if (win == 1)
            {
                cout << p1.Name << " Wins" << endl;
                p1.update_score();
            }
            else if (win == 0)
            {
                cout << p2.Name << " Wins" << endl;
                p2.update_score();
            }
            else
                cout << "~ Tie ~" << endl;

            getch();
            round++;
        }
        catch (int e)
        {
            // [ 400 ] Invalid Input
            if (e == 400)
            {
                cout << "\nInvalid Input plz Select from [ 1,2,3 ]\nEnter to play: ";
                getch();
            }
        }
    }

    // Show Final Winner
    if (p1.score > p2.score)
    {
        system("cls");
        Logo();
        cout << "\n You Win " << p1.Name << endl;
    }
    else if (p1.score < p2.score)
    {
        system("cls");
        Logo();
        cout << "\n"
             << p2.Name << " Wins\nBetter Luck Next Time :)" << endl;
    }
    else
    {
        system("cls");
        Logo();
        cout << "\n\n-+-+- TIE -+-+-";
    }

    PA: // If invalid input
    cout << "\n\nDo you want to play again [y/n] ?";
    cin >> YN;
    if (YN == "y")
        main();
    else if (YN == "n")
        exit(1);
    else
        goto PA;
    return 0;
}

// Display Basic & Necessary Stuff
// Include : [ Logo, current round, score board, sign Hand ]
void display(string p1name, string p2name, int r, int p1, int p2, int s1, int s2)
{
    system("cls"); // clear screen

    // Logo
    Logo();

    // Current Round
    printf("\n\t\t-+-+- Round %d -+-+-\n\n", r);

    // Score Board
    cout << "\t  [ " << s1 << " ] " << p1name << " -- [ " << s2 << " ] " << p2name << " \n\n";

    // Sign Hand
    show_hand(p1, p2);
    cout << "You\n\n";
}

void Logo()
{
    // Logo
    cout << "\t  ______       ______       _____ " << endl;
    cout << "\t  | ___ \\      | ___ \\     /  ___|" << endl;
    cout << "\t  | |_/ /      | |_/ /     \\ `--. " << endl;
    cout << "\t  |    /       |  __/       `--. \\" << endl;
    cout << "\t  | |\\ \\       | |         /\\__/ /" << endl;
    cout << "\t  \\_| \\_|      \\_|         \\____/ " << endl;
}

// Display Sign hand as per choice
void show_hand(int a, int b)
{
    // R=1, P=2, S=3
    switch (a * 10 + b)
    {
    case 11:
        cout << "     _______                            _______    " << endl;
        cout << "----'   ____)                          (____   '---" << endl;
        cout << "       (_____)                        (_____)      " << endl;
        cout << "       (_____)                        (_____)      " << endl;
        cout << "       (____)                          (____)      " << endl;
        cout << "----.__(___)                            (___)__.---" << endl;
        break;
    case 12:
        cout << "     _______                           ________    " << endl;
        cout << "----'   ____)                     ____(____    '---" << endl;
        cout << "       (_____)                   (______           " << endl;
        cout << "       (_____)                   (_______          " << endl;
        cout << "       (____)                     (_______         " << endl;
        cout << "----.__(___)                        (__________.---" << endl;
        break;
    case 13:
        cout << "     _______                            _______    " << endl;
        cout << "----'   ____)                     _____(____   '---" << endl;
        cout << "       (_____)                   (_______          " << endl;
        cout << "       (_____)                   (__________       " << endl;
        cout << "       (____)                          (____)      " << endl;
        cout << "----.__(___)                            (___)__.---" << endl;
        break;
    case 21:
        cout << "      _______                           _______    " << endl;
        cout << "----'    ____)____                     (____   '---" << endl;
        cout << "            ______)                   (_____)      " << endl;
        cout << "           _______)                   (_____)      " << endl;
        cout << "          _______)                     (____)      " << endl;
        cout << "----.__________)                        (___)__.---" << endl;
        break;
    case 22:
        cout << "      _______                          ________    " << endl;
        cout << "----'    ____)____                ____(____    '---" << endl;
        cout << "            ______)              (______           " << endl;
        cout << "           _______)              (_______          " << endl;
        cout << "          _______)                (_______         " << endl;
        cout << "----.__________)                    (__________.---" << endl;
        break;
    case 23:
        cout << "      _______                           _______    " << endl;
        cout << "----'    ____)____                _____(____   '---" << endl;
        cout << "            ______)              (_______          " << endl;
        cout << "           _______)              (__________       " << endl;
        cout << "          _______)                     (____)      " << endl;
        cout << "----.__________)                        (___)__.---" << endl;
        break;
    case 31:
        cout << "     _______                            _______    " << endl;
        cout << "----'   ____)____                      (____   '---" << endl;
        cout << "           ______)                    (_____)      " << endl;
        cout << "        __________)                   (_____)      " << endl;
        cout << "       (____)                          (____)      " << endl;
        cout << "----.__(___)                            (___)__.---" << endl;
        break;
    case 32:
        cout << "     _______                           ________    " << endl;
        cout << "----'   ____)____                 ____(____    '---" << endl;
        cout << "           ______)               (______           " << endl;
        cout << "        __________)              (_______          " << endl;
        cout << "       (____)                     (_______         " << endl;
        cout << "----.__(___)                        (__________.---" << endl;
        break;
    case 33:
        cout << "     _______                            _______    " << endl;
        cout << "----'   ____)____                 _____(____   '---" << endl;
        cout << "           ______)               (_______          " << endl;
        cout << "        __________)              (__________       " << endl;
        cout << "       (____)                          (____)      " << endl;
        cout << "----.__(___)                            (___)__.---" << endl;
        break;
    default:
        cout << "\n\n\n\n\n\n"
             << endl;
        break;
    }
}