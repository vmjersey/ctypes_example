#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#define MAX_WORDSIZE 14

struct wrtype{
	FILE *fh;
	int count;
	char **words;
        int max_buffer;
} wrtype;

struct wrtype *init_file(char *filename,int max_buffer){

	struct wrtype *wr = malloc(sizeof(wrtype));
	wr->fh = fopen(filename,"a");
        wr->max_buffer = max_buffer;
        wr->words = malloc(wr->max_buffer*sizeof(char*));
	//Initiallize all of the words
	for (int i=0; i<wr->max_buffer; i++){
		wr->words[i] = malloc(MAX_WORDSIZE*sizeof(char));
	}
	wr->count = 0;
	return wr;
}

int print_buffer(struct wrtype *wr){

        for (int i = 0; i < wr->count;i++){
                fprintf(wr->fh,"%s\n",wr->words[i]);
        }
}


int dump(struct wrtype *wr, int len,char **words){

	for (int i = 0;i<len;i++){
		if (wr->count == wr->max_buffer){
			print_buffer(wr);
			wr->count = 0;	
                }
		memset(wr->words[wr->count],0,MAX_WORDSIZE);
		int len = strlen(words[i]);
                memcpy(wr->words[wr->count],words[i],len);
		wr->count++;
	}
	return 0;
}


int cleanup(struct wrtype *wr){

	//Make sure all words are written
	if (wr->count != 0){
		print_buffer(wr);
	}

	fclose(wr->fh);
	for (int i = 0; i<wr->max_buffer;i++){
		free(wr->words[i]);
	}
	free(wr->words);
	free(wr);

  return 0;
}


