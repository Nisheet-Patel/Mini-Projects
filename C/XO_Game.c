#include <stdio.h>
#include <conio.h>
#include <string.h>
#include <ctype.h>
#include <unistd.h>
#define ASIZE 3

/*

A: 3 Rounds
B: 5 Rounds 
C: 10 Rounds

Choose Round :
*/

int _X, _Y;
char P1[30], P2[30];
int _SX = 0, _SO = 0;

int _get_pos_val(int b[][ASIZE], char);
int valid_move(int board[][ASIZE], char);
int choose_round();
void Game_title();
void Print_Board(int b[][ASIZE]);
int Check_Win(int b[][ASIZE]);
void Announce_Winer(char);

int main(int argc, char const *argv[])
{
    system("cls");
    // TURN : 0 = O, 1 = X
    // 2 = Empty, 3 = Invalid
    char Uin, TURN = 1;
    /* {{7, 8, 9}, 
        {4, 5, 6}, 
        {1, 2, 3 }} 
    */
    int i, ROUNDS, CW;

    Game_title();

    printf("\n\nX | Player 1 Name : ");
    gets(P1);
    printf("\nO | Player 2 Name : ");
    gets(P2);

    ROUNDS = choose_round();

    for (i = 0; i < ROUNDS; i++)
    {
        int j = 0;
        int board[3][3] = {{2, 2, 2}, {2, 2, 2}, {2, 2, 2}};
        while (j < 9)
        {
            //clear Screen
            system("cls");

            Game_title();

            printf("\n\n%s | X : %d", P1, _SX);
            printf("\n%s | O : %d\n", P2, _SO);

            // Print TURN OX
            if (TURN == 0)
                printf("\nTurn : O\n\n");
            else if (TURN == 1)
                printf("\nTurn : X\n\n");

            // Display Board
            Print_Board(board);

            // User Input
            puts("\n__");
            Uin = getch();

            // check valid move and update and change TURN
            if (valid_move(board, Uin) == 1)
            {
                board[_X][_Y] = TURN;
                if (TURN == 0)
                    TURN = 1;
                else
                    TURN = 0;
                j++;
            }
            else
            {
                printf("\n| Invalid Input |");
                printf("\n-> Plz Enter Number Accordingly \n");
                printf("7 | 8 | 9\n---------\n4 | 5 | 6\n---------\n1 | 2 | 3\n");
                sleep(2);
            }

            // Check Winner
            CW = Check_Win(board);
            if (CW == 0)
            {
                system("cls");
                Print_Board(board);
                printf("\n\n%s | O Wins This Round", P2);
                _SO++;
                TURN = 0;
                j++;
                break;
            }
            else if (CW == 1)
            {
                system("cls");
                Print_Board(board);
                printf("\n\n%s | X Wins This Round", P1);
                _SX++;
                TURN = 1;
                j++;
                break;
            }
            else if (j == 8)
            {
                system("cls");
                Print_Board(board);
                printf("\n\n--> TIE <--");
                break;
            }
        }
        sleep(2);
    }
    if (_SX > _SO)
        Announce_Winer('X');
    else if (_SX < _SO)
        Announce_Winer('O');
    else
        Announce_Winer('T');
    sleep(2);
    return 0;
}

int valid_move(int board[][ASIZE], char n)
{
    // 1 = True, 0 = False
    if (_get_pos_val(board, n) == 2)
        return 1;
    return 0;
}

int _get_pos_val(int b[][ASIZE], char n)
{
    // Return Values as per number input
    switch (n)
    {
    case '7':
        _X = 0, _Y = 0;
        return b[0][0];
    case '8':
        _X = 0, _Y = 1;
        return b[0][1];
    case '9':
        _X = 0, _Y = 2;
        return b[0][2];
    case '4':
        _X = 1, _Y = 0;
        return b[1][0];
    case '5':
        _X = 1, _Y = 1;
        return b[1][1];
    case '6':
        _X = 1, _Y = 2;
        return b[1][2];
    case '1':
        _X = 2, _Y = 0;
        return b[2][0];
    case '2':
        _X = 2, _Y = 1;
        return b[2][1];
    case '3':
        _X = 2, _Y = 2;
        return b[2][2];
    default:
        break;
    }
    return 3;
}

int choose_round()
{
    printf("\nA: 3 Rounds\nB: 5 Rounds\nC: 10 Rounds\n\nChoose Round : ");
    char c;

    while (1)
    {
        c = tolower(getch());
        putchar(c);

        switch (c)
        {
        case 'a':
            return 3;
        case 'b':
            return 5;
        case 'c':
            return 10;
        }
    }
    return 0;
}

void Print_Board(int b[][ASIZE])
{
    int i, j;

    for (i = 0; i < ASIZE; i++)
    {
        for (j = 0; j < ASIZE; j++)
        {
            if (b[i][j] == 0)
                printf(" O ");
            else if (b[i][j] == 1)
                printf(" X ");
            else
                printf("   ");
            if (j < 2)
                printf("|");
        }
        if (i < 2)
            printf("\n-----------\n");
    }
}

int Check_Win(int b[][ASIZE])
{
    int i, j, k;
    for (k = 0; k <= 1; k++)
    {
        for (i = 0; i < 3; i++)
        {
            // ROWs
            if (b[0][i] == k && b[1][i] == k && b[2][i] == k)
                return k;
            //COLs
            if (b[i][0] == k && b[i][1] == k && b[i][2] == k)
                return k;
            //DIAGONALs
            if (b[0][2] == k && b[1][1] == k && b[2][0] == k)
                return k;
            if (b[0][0] == k && b[1][1] == k && b[2][2] == k)
                return k;
        }
    }
    return 2;
}

void Announce_Winer(char w)
{
    system("cls");
    printf("\n\n%s | X : %d", P1, _SX);
    printf("\n%s | O : %d\n", P2, _SO);
    if (w == 'X')
    {
        printf("\n __   __   __          ___           ");
        printf("\n \\ \\ / /   \\ \\        / (_)          ");
        printf("\n  \\ V /     \\ \\  /\\  / / _ _ __  ___ ");
        printf("\n   > <       \\ \\/  \\/ / | | '_ \\/ __|");
        printf("\n  / . \\       \\  /\\  /  | | | | \\__ \\");
        printf("\n /_/ \\_\\       \\/  \\/   |_|_| |_|___/");
    }
    else if (w == 'O')
    {
        printf("\n   ____     __          ___           ");
        printf("\n  / __ \\    \\ \\        / (_)          ");
        printf("\n | |  | |    \\ \\  /\\  / / _ _ __  ___ ");
        printf("\n | |  | |     \\ \\/  \\/ / | | '_ \\/ __|");
        printf("\n | |__| |      \\  /\\  /  | | | | \\__ \\");
        printf("\n  \\____/        \\/  \\/   |_|_| |_|___/");
    }
    else if (w == 'T')
    {
        printf("\n  _______ _____ ______ ");
        printf("\n |__   __|_   _|  ____|");
        printf("\n    | |    | | | |__   ");
        printf("\n    | |    | | |  __|  ");
        printf("\n    | |   _| |_| |____ ");
        printf("\n    |_|  |_____|______|");
    }
    printf("\n\n\nCreator : Nisheet");
}

void Game_title()
{
    printf("\n  _______ _____ _____   _______       _____   _______ ____  ______ ");
    printf("\n |__   __|_   _/ ____| |__   __|/\\   / ____| |__   __/ __ \\|  ____|");
    printf("\n    | |    | || |         | |  /  \\ | |         | | | |  | | |__   ");
    printf("\n    | |    | || |         | | / /\\ \\| |         | | | |  | |  __|  ");
    printf("\n    | |   _| || |____     | |/ ____ \\ |____     | | | |__| | |____ ");
    printf("\n    |_|  |_____\\_____|    |_/_/    \\_\\_____|    |_|  \\____/|______|");
}
