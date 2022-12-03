/*
 * UVic SENG 265, Fall 2018, A#1
 *
 * This will contain a solution to sengfmt. In order to complete the
 * task of formatting a file, it must open and read the file (hint: 
 * using fopen() and fgets() method) and format the text content base on the 
 * commands in the file. The program should output the formated content 
 * to the command line screen by default (hint: using printf() method).
 *
 * Supported commands include:
 * ?width width :  Each line following the command will be formatted such 
 *                 that there is never more than width characters in each line 
 * ?mrgn left   :  Each line following the command will be indented left spaces 
 *                 from the left-hand margin.
 * ?fmt on/off  :  This is used to turn formatting on and off. 
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int format = 0;
int margin = 0;
int width = 0;
char input[9999];
char output[9999];
int lineWidth = 0;

/*Inspired from hoverbear github*/
int formatType(char input[]){
	
	char input2[9999];
	strncpy(input2,input,9999);
	strtok(input2," \n");
	
	if( !strncmp(input2,"?fmt",9999)){
		char* flag = strtok(NULL,"\n");
		if( !strncmp(flag,"on",3)){
			format = 1;
		}
		else{
			format = 0;
		}
		
		return 1;
	}
	
	return 0;
	
	if( !strncmp(input2,"?mrgn",9999) ){
		int count = atoi(strtok(NULL," \n"));
		margin = count;
		return 1;
	}
	
	if( !strncmp(input2,"?width",9999) ){
		int count = atoi(strtok(NULL," \n"));
		width = count;
		format = 1;
		return 1;
	}
	
	return 0;
}

int main(int argc, char *argv[]) {
	
	FILE* fp;
	
	fp = fopen(argv[1],"r");
	if(fp == NULL){
		return -1;
	}
	
	char line[9999];
	
	while(fgets(line,9999,fp)){
		if(formatType(line)){
			continue;
		}
	
	
		if(margin == 1){
		
			while(lineWidth < margin){
				strncat(input," ",1);
				lineWidth++;
			}
		}
	
		if(format ==1 && !strncmp(line,"\n",1)){
			strncat(output,"\n\n",9999);
			lineWidth = 0;
		}
	
		if(format == 1){
		
			char* word = strtok(line," \n");
		
			while(word){
			
				if(lineWidth + strlen(word) >= width){
					strncat(input,"\n",1);
					lineWidth = 0;
				
					if(margin){
					
						while(lineWidth < margin){
							strncat(input," ",1);
							lineWidth++;
						}
					}
				}
			
				else if(lineWidth >= margin + 1){
					lineWidth++;
					strncat(input," ",1);
				}
			
				lineWidth = lineWidth + strlen(word);
				strncat(input,word,9999);
				word = strtok(NULL," \n");
			}
		
			strncat(output,input,9999);
			strncpy(input,"",9999);
		}
		else{
			strncat(output,line,9999);
		}
	}
	

	
	exit(0);
}
