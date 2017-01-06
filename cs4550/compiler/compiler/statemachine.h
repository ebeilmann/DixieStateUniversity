#pragma once
#include "token.h"
#include "debug.h"

enum MachineState {
	START_STATE, CANTMOVE_STATE,
	//whitespace
	WHITESPACE_STATE, SPACE_STATE, TAB_STATE, REUTRN_STATE,
	/*Reserved Words:*/
	VOID_STATE, MAIN_STATE, INT_STATE, COUT_STATE, BOOL_STATE, TRUE_STATE, FALSE_STATE,REPEAT_STATE,
	/*Relational Operators:*/
	LESS_STATE, LESSEQUAL_STATE, GREATER_STATE, GREATEREQUAL_STATE, EQUAL_STATE, NOT_STATE, NOTEQUAL_STATE,NOTVALUE_STATE,NEGATE_STATE,
	/*Other Operators:*/
	INSERTION_STATE, ASSIGNMENT_STATE, PLUS_STATE, MINUS_STATE, TIMES_STATE, DIVIDE_STATE, PLUSEQUAL_STATE, MINUSEQUAL_STATE,TIMESEQUAL_STATE,
	/*Other Characters:*/
	SEMICOLON_STATE, LPAREN_STATE, RPAREN_STATE, LCURLY_STATE, RCURLY_STATE, OR_STATE, AND_STATE,
	/*Other Token Types:*/
	BEGIN_STATE,END_STATE,IDENTIFIER_STATE, INTEGER_STATE, ENDFILE_STATE,
	//other
	COMMENT_LINE_STATE, COMMENT_START_STATE, COMMENT_END_STATE, BAD_STATE, LAST_STATE
};
enum CharacterType {
	LETTER_CHAR, DIGIT_CHAR,
	//whitespace
	WHITESPACE_CHAR, SPACE_CHAR, TAB_CHAR, RETURN_CHAR,
	/*Relational Operators:*/
	LESS_CHAR, LESSEQUAL_CHAR, GREATER_CHAR, GREATEREQUAL_CHAR, EQUAL_CHAR, NOT_CHAR, NOTEQUAL_CHAR,
	/*Other Operators:*/
	INSERTION_CHAR, ASSIGNMENT_CHAR, PLUS_CHAR, MINUS_CHAR, TIMES_CHAR, DIVIDE_CHAR,
	/*Other Characters:*/
	SEMICOLON_CHAR, LPAREN_CHAR, RPAREN_CHAR, LCURLY_CHAR, RCURLY_CHAR, OR_CHAR, AND_CHAR,
	/*Other Token Types:*/
	BEGIN_CHAR,END_CHAR,IDENTIFIER_CHAR, INTEGER_CHAR, ENDFILE_CHAR,
	//other
	COMMENT_CHAR, BAD_CHAR, LAST_CHAR
};
class StateMachineClass
{
public:
	StateMachineClass();
	MachineState UpdateState(char currentCharacter, TokenType & correspondingTokenType);
private:
	MachineState mCurrentState;
	// The matrix of legal moves:
	MachineState mLegalMoves[LAST_STATE][LAST_CHAR];
	// Which end-machine-states correspond to which token types. (non end states correspond to the BAD_TOKEN token type)
	TokenType mCorrespondingTokenTypes[LAST_STATE];
};
