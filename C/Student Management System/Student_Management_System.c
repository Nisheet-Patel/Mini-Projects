#include <stdio.h>
#include <string.h>
#include <conio.h>
#include <stdlib.h>

void logo();
void print_stu(char *, char *, int, int, int);
void result_title();

int main()
{
    FILE *fi;
    char name[43], sname[43], uname[43];
    int sem, feesp, user, rol;
    int urol;
    fi = fopen("Data.csv", "r");
    do
    {
        system("cls");

        logo();

        printf("\n\n[1] Find By Name\n");
        printf("[2] Find By Roll number\n");
        printf("[3] Fees Paid\n");
        printf("[4] Fees Not Paid\n");
        printf("[5] Print Student Data\n");
        printf("[0] Exit\n:");
        scanf("%d", &user);

        if (user == 1) // Find by name
        {
            system("cls");
            printf("FIND STUDENT BY NAME\n");
            puts("\nEnter Name?");
            scanf("%s", &uname);

            rewind(fi);
            result_title();
            while (!feof(fi))
            {
                fscanf(fi, "%d, %d, %d,%s %s", &rol, &sem, &feesp, &sname, &name);
                if (strcmp(strlwr(uname), strlwr(name)) == 0)
                    print_stu(sname,name, rol, sem, feesp);
            }
            getch();
        }
        else if (user == 2) // Find by roll number
        {
            system("cls");
            printf("FIND STUDENT BY ROLL NUMBER\n");
            puts("\nEnter Roll no?");
            scanf("%d", &urol);

            rewind(fi);
            result_title();
            while (!feof(fi))
            {
                fscanf(fi, "%d, %d, %d,%s %s", &rol, &sem, &feesp, &sname, &name);
                if (urol == rol)
                {
                    print_stu(sname,name, rol, sem, feesp);
                    break;
                }
            }
            getch();
        }
        else if (user == 3) // Find by roll number
        {
            int p = 0, np = 0;
            system("cls");
            printf("FEES PAID\n");

            rewind(fi);
            result_title();
            while (!feof(fi))
            {
                fscanf(fi, "%d, %d, %d,%s %s", &rol, &sem, &feesp, &sname, &name);
                if (feesp)
                {
                    print_stu(sname,name, rol, sem, feesp);
                    p++;
                }
                else
                    np++;
            }
            printf("\n\nFees Paid     : %d\nFees Not Paid : %d\nTotal Student : %d", p, np, p + np);
            getch();
        }
        else if (user == 4) // Find by roll number
        {
            int p = 0, np = 0;
            system("cls");
            printf("FEES NOT PAID\n");

            rewind(fi);
            result_title();
            while (!feof(fi))
            {
                fscanf(fi, "%d, %d, %d,%s %s", &rol, &sem, &feesp, &sname, &name);
                if (!feesp)
                {
                    print_stu(sname,name, rol, sem, feesp);
                    np++;
                }
                else
                    p++;
            }
            printf("\n\nFees Paid     : %d\nFees Not Paid : %d\nTotal Student : %d", p, np, p + np);
            getch();
        }
        else if (user == 5) // Print Student Data
        {
            system("cls");
            printf("STUDENT DATA\n");
            rewind(fi);
            result_title();
            while (!feof(fi))
            {
                fscanf(fi, "%d, %d, %d,%s %s", &rol, &sem, &feesp, &sname, &name);
                print_stu(sname,name, rol, sem, feesp);
            }
            getch();
        }
        else if (user == 0)
            exit(1);
    } while (user <= 5);
    fclose(fi);
}

void print_stu(char sname[],char name[], int rol, int sem, int fees)
{
    if (fees)
        printf("\n%-8d   %-12s   %-12s   %-5d   %-12s", rol, sname,name, sem, "Yes");
    else
        printf("\n%-8d   %-12s   %-12s   %-5d   %-12s", rol, sname,name, sem, "No");
}

void result_title()
{
    printf("\n - - - - - - - - - - Result Found - - - - - - - - -\n");
    printf("%-8s   %-12s   %-12s   %-5s   %-12s\n", "Roll No.","Surname", "Name", "SEM", "Fees");
}

void logo()
{
    printf("\n   _____ _             _            _     __  __                                   ");
    printf("\n  / ____| |           | |          | |   |  \\/  |                                  ");
    printf("\n | (___ | |_ _   _  __| | ___ _ __ | |_  | \\  / | __ _ _ __   __ _  __ _  ___ _ __ ");
    printf("\n  \\___ \\| __| | | |/ _` |/ _ \\ '_ \\| __| | |\\/| |/ _` | '_ \\ / _` |/ _` |/ _ \\ '__|");
    printf("\n  ____) | |_| |_| | (_| |  __/ | | | |_  | |  | | (_| | | | | (_| | (_| |  __/ |   ");
    printf("\n |_____/ \\__|\\__,_|\\__,_|\\___|_| |_|\\__| |_|  |_|\\__,_|_| |_|\\__,_|\\__, |\\___|_|   ");
    printf("\n                                                                    __/ |          ");
    printf("\n                                                                   |___/           ");
}