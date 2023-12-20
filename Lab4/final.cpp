// Assignment 4

// This implementation uses manhattan distance as heuristics.
// It also uses a slightly modified concept of hill climbing search.

// The code looks for possible states by bello order
// UP -> RIGHT -> DOWN -> LEFT

// Using Simulated Annealing would have been better but we could not
// finish the code using SA for the time being.

// This code belongs to Sajid Anam Ifti


#include <bits/stdc++.h>
#include <cstdlib>

using namespace std;

char initial[3][3], goal[3][3];
int step = 0;

// Function to return the position of an element in the 2D array
// 1. c is the charecter to find
// 2. state[3][3] is the array to search
// 3. arr[] is the array to return results. It should be like arr[2]
void position(char c, char state[3][3], int arr[])
{
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            if (state[i][j] == c)
            {
                arr[0] = i;
                arr[1] = j;
            }
        }
    }
}

// Function to calculate Manhattan Distance of a state
// 1. current[3][3] is the state
int mhd(char current[3][3])
{
    int distance = 0, arr[2];

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            if (current[i][j] == 'X')
            {
                continue;
            }

            position(current[i][j], goal, arr);

            int d = abs(i - arr[0]) + abs(j - arr[1]);

            distance = distance + d;
        }
    }

    return distance;
}

// Function that prints the steps
// current is the array to print
void printStep(char current[3][3])
{
    cout << "Step #" << step << endl;
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            cout << current[i][j] << " ";
        }
        cout << endl;
    }
}

// Function to return if the coordinates are valid
bool isValid(int arr[2])
{
    if (arr[0] >= 0 && arr[0] < 3 && arr[1] >= 0 && arr[1] < 3)
    {
        return true;
    }
    else
    {
        return false;
    }
}

// Function to compare previous and next positions
bool notEqual(int arr[2], int arr2[2])
{
    if (arr[0] == arr2[0] && arr[1] == arr2[1])
    {
        return false;
    }
    else
    {
        return true;
    }
}

// Funtion that solves the puzzle
void puzzle()
{
    int prev_pos[2];

    char current[3][3];

    copy(&initial[0][0], &initial[0][0] + 3 * 3, &current[0][0]);

    position('X', current, prev_pos);

    step++;
    printStep(current);

    while (true)
    {
        int left_pos[2], up_pos[2], right_pos[2], down_pos[2], curr_pos[2], curr_mhd = 10000;

        char left_state[3][3], temp_state[3][3], right_state[3][3], up_state[3][3], down_state[3][3];

        position('X', current, curr_pos);

        int x = curr_pos[0];
        int y = curr_pos[1];

        // up shift
        up_pos[0] = x - 1;
        up_pos[1] = y;

        if (isValid(up_pos) && notEqual(up_pos, prev_pos))
        {
            copy(&current[0][0], &current[0][0] + 3 * 3, &up_state[0][0]);

            swap(up_state[x][y], up_state[x - 1][y]);

            int umhd = mhd(up_state);

            if (umhd <= curr_mhd)
            {
                curr_mhd = umhd;

                copy(&up_state[0][0], &up_state[0][0] + 3 * 3, &temp_state[0][0]);
            }
        }

        // right shift
        right_pos[0] = x;
        right_pos[1] = y + 1;

        if (isValid(right_pos) && notEqual(right_pos, prev_pos))
        {
            copy(&current[0][0], &current[0][0] + 3 * 3, &right_state[0][0]);

            swap(right_state[x][y], right_state[x][y + 1]);

            int rmhd = mhd(right_state);

            if (rmhd <= curr_mhd)
            {
                curr_mhd = rmhd;

                copy(&right_state[0][0], &right_state[0][0] + 3 * 3, &temp_state[0][0]);
            }
        }
        // down shift
        down_pos[0] = x + 1;
        down_pos[1] = y;

        if (isValid(down_pos) && notEqual(down_pos, prev_pos))
        {
            copy(&current[0][0], &current[0][0] + 3 * 3, &down_state[0][0]);

            swap(down_state[x][y], down_state[x + 1][y]);

            int dmhd = mhd(down_state);

            if (dmhd <= curr_mhd)
            {
                curr_mhd = dmhd;

                copy(&down_state[0][0], &down_state[0][0] + 3 * 3, &temp_state[0][0]);
            }
        }
        // left shift
        left_pos[0] = x;
        left_pos[1] = y - 1;

        if (isValid(left_pos) && notEqual(left_pos, prev_pos))
        {
            copy(&current[0][0], &current[0][0] + 3 * 3, &left_state[0][0]);

            swap(left_state[x][y], left_state[x][y - 1]);

            int lmhd = mhd(left_state);

            if (lmhd <= curr_mhd)
            {
                curr_mhd = lmhd;

                copy(&left_state[0][0], &left_state[0][0] + 3 * 3, &temp_state[0][0]);
            }
        }
        
        // other
        prev_pos[0] = curr_pos[0];
        prev_pos[1] = curr_pos[1];

        copy(&temp_state[0][0], &temp_state[0][0] + 3 * 3, &current[0][0]);

        step++;
        printStep(current);

        if (curr_mhd == 0)
        {
            break;
        }

        // end of while
    }
}

// Main function
int main()
{

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            cin >> initial[i][j];
        }
    }

    cout << endl;

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            cin >> goal[i][j];
        }
    }

    puzzle();

    return 0;
}