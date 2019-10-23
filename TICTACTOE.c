/* TIC TAC TOE VERSION 1.0 
made by SOUMYAJIT SINHA , created 17-sept-2019
last updated - 27-sept-2019
*/

#include<stdio.h>
int ttt[3][3];
int val;

char player1[20], player2[20];


int asklocation()
{
	int location; 
	printf("The location you want\n");
	scanf("%d", &location);
	if (location>0 && location<10)
	{
		return location;
	}
	else
	{
		printf("Re-enter location.\n");
		return asklocation();
	}
	
}


user1()
{
	int value, numbercondition;
	printf("\nPlayer 1 %s\n", player1);
	value=asklocation();
	numbercondition=checkvalue(value);
	if (numbercondition==10)
	{
		putvalue(1, value);
	}
	else
	{
		printf("Cant place in that location.\n");
		user1();
		
	}
}

user2()
{
	int value, numbercondition;
	printf("\nPlayer 2 %s\n", player2);
	value=asklocation();
	numbercondition=checkvalue(value);
	if (numbercondition==10)
	{
		putvalue(2, value);
	}
	else
	{
		printf("Cant place in that location.\n");
		user2();
		
	}
}

putvalue(int x, int y)
{
	switch (y)
	{
		case 1:
			ttt[0][0]=x;
			break;

		case 2:
			ttt[0][1]=x;
			break;
			
		case 3:
			ttt[0][2]=x;
			break;
		
		case 4:
			ttt[1][0]=x;
			break;

		case 5:
			ttt[1][1]=x;
			break;
			
		case 6:
			ttt[1][2]=x;
			break;
			
		case 7:
			ttt[2][0]=x;
			break;

		case 8:
			ttt[2][1]=x;
			break;
			
		case 9:
			ttt[2][2]=x;
			break;
			
				
		default:
			printf("Default");						
	}
}



int checkvalue(int value)
{
	switch (value)
	{
		case 1:
			if (ttt[0][0]==0)
				return 10;
			else
				return 5;	
			break;

		case 2:
			if (ttt[0][1]==0)
				return 10;
			else
				return 5;	
			break;
			
			
		case 3:
			if (ttt[0][2]==0)
				return 10;
			else
				return 5;	
			break;
		
		case 4:
			if (ttt[1][0]==0)
				return 10;
			else
				return 5;	
			break;
		
		case 5:
			if (ttt[1][1]==0)
				return 10;
			else
				return 5;	
			break;
		
		case 6:
			if (ttt[1][2]==0)
				return 10;
			else
				return 5;	
			break;
		
		case 7:
			if (ttt[2][0]==0)
				return 10;
			else
				return 5;	
			break;
		
		case 8:
			if (ttt[2][1]==0)
				return 10;
			else
				return 5;	
			break;
		
		case 9:
			if (ttt[2][2]==0)
				return 10;
			else
				return 5;	
			break;
			
		default:
			return 5;						
	}
}

display()
{
	printf("\nThe Matrix so formed is :-\n %d\t| %d\t| %d\n---------------------\n %d\t| %d\t| %d\n---------------------\n %d\t| %d\t| %d\n", ttt[0][0], ttt[0][1], ttt[0][2], ttt[1][0], ttt[1][1], ttt[1][2], ttt[2][0], ttt[2][1], ttt[2][2]);
}

 int check()
{
	//1=2=3
	if(ttt[0][0]==ttt[0][1] && ttt[0][1]==ttt[0][2] && ttt[0][0]>0 && ttt[0][1]>0 && ttt[0][2]>0)
	{
		return 10;
	}
	
	//4=5=6
	else if(ttt[1][0]==ttt[1][1] && ttt[1][1]==ttt[1][2] && ttt[1][0]>0 && ttt[1][1]>0 && ttt[1][2]>0)
	{
		return 10;
	}
	
	//7=8=9
	else if(ttt[2][0]==ttt[2][1] && ttt[2][1]==ttt[2][2] && ttt[2][0]>0 && ttt[2][1]>0 && ttt[2][2]>0)
	{
		return 10;
	}
	
	//1=4=7
	else if(ttt[0][0]==ttt[1][0] && ttt[1][0]==ttt[2][0] && ttt[0][0]>0 && ttt[1][0]>0 && ttt[2][0]>0)
	{
		return 10;
	}
	
	//2=5=8
	else if(ttt[0][1]==ttt[1][1] && ttt[1][1]==ttt[2][1] && ttt[0][1]>0 && ttt[1][1]>0 && ttt[2][1]>0)
	{
		return 10;
	}
	
	//3=6=9
	else if(ttt[0][2]==ttt[1][2] && ttt[1][2]==ttt[2][2] && ttt[0][2]>0 && ttt[2][1]>0 && ttt[2][2]>0)
	{
		return 10;
	}
	
	//1=5=9
	else if(ttt[0][0]==ttt[1][1] && ttt[1][1]==ttt[2][2] && ttt[0][0]>0 && ttt[1][1]>0 && ttt[2][2]>0)
	{
		return 10;
	}
	
	//3=5=7
	else if(ttt[0][2]==ttt[1][1] && ttt[1][1]==ttt[2][0] && ttt[0][2]>0 && ttt[1][1]>0 && ttt[2][0]>0)
	{
		return 10;
	}
	
	else
	{
		return 0;
	}
}


void main()
{
	int c=0, count=0;
	
	ttt[0][0]=0;
	ttt[0][1]=0;
	ttt[0][2]=0;
	ttt[1][0]=0;
	ttt[1][1]=0;
	ttt[1][2]=0;
	ttt[2][0]=0;
	ttt[2][1]=0;
	ttt[2][2]=0;
	printf("Hello. I am Mr.Tic-Tac-Toe;.\nI have been created by Soumyajit Sinha.\nLets Play a game of tictactoe.\n\n\nPlayer 1. Insert your name.\n");
	scanf("%s", player1);
	printf("Player 2. insert your name.\n");
	scanf("%s", player2);
	
	printf("\n\nTHE TIC TAC TOE MATRIX WILL BE PRESENT IN FOR:-\n 1\t|2\t|3\n---------------------\n4\t|5\t|6\n---------------------\n7\t|8\t|9\nTHe player needs to place the location of their input as '1' by player one and'2' by player 2.\n");
	
	for(;;)
	{
		user1();
		display();
		c=check();
		if (c==10)
		{
			printf("Player 1, i.e %s is Winner.", player1);
			break; 
		}
		else
		{
			count++;
		}
		
		if (count==9)
		{
			printf("Well Played! IT'S A DRAW!!\n'");
			break;
		}
		else
		{
			
		}
		
		
		user2();
		display();
		c=check();
		if (c==10)
		{
			printf("Player 2, i.e %s is Winner.", player2);
			break; 
		}
		else
		{
			count++;
		}
		
		if (count==9)
		{
			printf("Well Played! IT'S A DRAW!!\n'");
			break;
		}
		else
		{
			
		}
	}
}
