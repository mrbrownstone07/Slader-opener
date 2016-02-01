#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(int argc, char const *argv[])
{
        printf("This is slader opener. Write \"exit\" to quit\n");
	char page[10],question[10];
        // Takes input of pages number
        printf("Page number: ");
	scanf("%s",page);
        // takes input of question number
	printf("Your page number is: %s\n",page );
        printf("Question number: ");
        scanf("%s",question);
	printf("Your question number: %s\n",question );
        // This is the basic link of slader. Concatenate our inputs to end of this string.
        char link[500]="http://www.slader.com/textbook/9780495011668-stewart-calculus-early-transcendentals-6th-edition/";
        // Concatenate them all
        strcat(link,page);
        strcat(link,"/exercises/");
        strcat(link,question);
        // Command is the xdg-open website-url to open website on terminal
        char command[] = "xdg-open ";
        strcat(command,link);
        system(command);
        


	return 0;
}
