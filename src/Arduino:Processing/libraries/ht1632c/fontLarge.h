/***********************************************************************
 * fontLarge.h - proportional characters defined in a 14 bit high by max. 11 bit wide grid;
 *		  	   - If highest bit not set then ignore the empty values;	
 *             - Used for displaying texts on 24x16 display of Wise Clock 3;
 * Copyright Aug 1/2011, by FlorinC(http://timewitharduino.blogspot.com/)
 *   Copyrighted and distributed under the terms of the Berkeley license
 *   (copy freely, but include this notice of original author.)
 ***********************************************************************
 */

//*********************************************************************************************************
// Display scrolling text with large 14 bit high by 2-11 bit wide proportional font
/*
void WiseClock3::displayLargeScrollingLine()
{
	int leftCol, tmpPos, x;

	// shift the 14 bit high characters one character to the left, 1 character is 2 - 11 bits wide;
	for (leftCol = 0; leftCol > -12; --leftCol)	
	{
		x = leftCol;
		tmpPos = crtPos;
		do
		{
			x = ht1632_putLargeChar(x, 1, ((tmpPos < strlen(msgLine)) ? msgLine[tmpPos] : ' '), crtColor);
			++tmpPos;
		}	
		while ((x < X_MAX + 1) && (x != 0));		// fill display with 32 dots and stop if 1 first char is moved out of the display;	
		delay(40 - nSpeed * 10);
		if (x == 0)
			break;									// we have moved the first complete character so stop;
	}
	++crtPos;
}


int ht1632_putLargeChar(int x, int y, char c, byte color)
{
	// fonts defined for ascii 32 and beyond (index 0 in font array is ascii 32);
	byte charIndex, col, row;
	
	// replace undisplayable characters with blank;
	if (c < 32 || c > 127)
	{
		charIndex	=	0;
	}
	else
	{
		charIndex	=	c - 32;
	}

	// move character definition, pixel by pixel, onto the display;
	// Fonts are defined as up to 14 bit per row and max. 11 columns;
	// first row is always zero to create the space between the characters;
	
	for (col=0; col < 11; ++col)					// max 11 columns;
	{
		uint16_t dots = pgm_read_word_near(&largeFont[charIndex][col]);
		if (dots == 0) 								// stop if all bits zero;
			break;
	
		for (row=0; row < 14; row++) 
		{
			if (dots & (0x4000 >> row))    			// max 14 rows;
				plot(x+col, y+row, color);
			else 
				plot(x+col, y+row, color & PUTINSNAPSHOTRAM);
		}
	}
	return x+col;
}


*/
//*********************************************************************************************************
//*	Edit History, started October, 2011
//*	please put your initials and comments here anytime you make changes
//*********************************************************************************************************
//* Oct. 15/11 (rp) First version
//*
//*
//*********************************************************************************************************


// define all ascii characters starting with 32 (blank);
uint16_t  PROGMEM largeFont[96][11] = {

  {
    0b1000000000000000,  // blank 6 dots wide 
    0b1000000000000000,
    0b1000000000000000,
    0b1000000000000000,
    0b1000000000000000,
    0b1000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // !
    0b1000000000000000,
    0b1111111111001100,
    0b1111111111001100,
    0b1000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // "
    0b1011010000000000,
    0b1011100000000000,
    0b1000000000000000,
    0b1011010000000000,
    0b1011100000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // #
    0b1000110001100000,
    0b1000110001100000,
    0b1111111111111100,
    0b1000110001100000,
    0b1000110001100000,
    0b1111111111111100,
    0b1000110001100000,
    0b1000110001100000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // $
    0b1000111000100000,
    0b1001000100010000,
    0b1111111111111100,
    0b1111111111111100,
    0b1001000100010000,
    0b1000100011100000,
    0b1000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // %
    0b1000000000000000,
    0b1011000000001100,
    0b1011000000111100,
    0b1000000011110000,
    0b1000001111000000,
    0b1000111100000000,
    0b1011110000001100,
    0b1011000000001100,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // &
    0b1000000000000000,
    0b1011110011111000,
    0b1111111111111100,
    0b1110011100001100,
    0b1111111110001100,
    0b1011110111111100,
    0b1000000001111000,
    0b1000000000110000,
    0b1000000000010000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // '
    0b1000000000000000,
    0b1011010000000000,
    0b1011100000000000,
    0b1000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // (
    0b1001111111110000,
    0b1011111111111000,
    0b1111000000011100,
    0b1110000000001100,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // )
    0b1110000000001100,
    0b1111000000011100,
    0b1011111111111000,
    0b1001111111110000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // *
    0b1000000100000000,
    0b1000010101000000,
    0b1000001110000000,
    0b1000111111100000,
    0b1000001110000000,
    0b1000010101000000,
    0b1000000100000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // +
    0b1000001100000000,
    0b1000001100000000,
    0b1001111111100000,
    0b1001111111100000,
    0b1000001100000000,
    0b1000001100000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // ,
    0b1000000000000000,
    0b1000000000011010,
    0b1000000000011100,
    0b1000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // -
    0b1000000000000000,
    0b1000000011000000,
    0b1000000011000000,
    0b1000000011000000,
    0b1000000011000000,
    0b1000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // .
    0b1000000000000000,
    0b1000000000001100,
    0b1000000000001100,
    0b1000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // /
    0b1000000000001100,
    0b1000000000111100,
    0b1000000011110000,
    0b1000001111000000,
    0b1000111100000000,
    0b1011110000000000,
    0b1011000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // 0
    0b1011111111111000,
    0b1111111111111100,
    0b1110000000001100,
    0b1110000000001100,
    0b1110000000001100,
    0b1110000000001100,
    0b1111111111111100,
    0b1011111111111000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // 1
    0b1001000000001100,
    0b1011000000001100,
    0b1111111111111100,
    0b1111111111111100,
    0b1000000000001100,
    0b1000000000001100,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // 2
    0b1011000111111100,
    0b1111001111111100,
    0b1110001100001100,
    0b1110001100001100,
    0b1110001100001100,
    0b1111111100001100,
    0b1011111000001100,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // 3
    0b1011000000011000,
    0b1111001100011100,
    0b1110001100001100,
    0b1110001100001100,
    0b1110001100001100,
    0b1111111111111100,
    0b1011110011111000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // 4
    0b1111111100000000,
    0b1111111100000000,
    0b1000001100000000,
    0b1000001100000000,
    0b1000001100000000,
    0b1111111111111100,
    0b1111111111111100,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // 5
    0b1111111000011000,
    0b1111111100011100,
    0b1110001100001100,
    0b1110001100001100,
    0b1110001100001100,
    0b1110001111111100,
    0b1110000111111000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // 6
    0b1011111111111000,
    0b1111111111111100,
    0b1110001100001100,
    0b1110001100001100,
    0b1110001100001100,
    0b1110001111111100,
    0b1010000111111000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // 7
    0b1110000000000000,
    0b1110000000000000,
    0b1110000011111100,
    0b1110000111111100,
    0b1110001100000000,
    0b1111111000000000,
    0b1111110000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // 8
    0b1011110011111000,
    0b1111111111111100,
    0b1110001100001100,
    0b1110001100001100,
    0b1110001100001100,
    0b1111111111111100,
    0b1011110011111000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // 9
    0b1011111000001000,
    0b1111111100001100,
    0b1110001100001100,
    0b1110001100001100,
    0b1110001100001100,
    0b1111111111111100,
    0b1011111111111000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // :
    0b1000000000000000,
    0b1000111001110000,
    0b1000111001110000,
    0b1000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // ;
    0b1000000000000000,
    0b1000111001110100,
    0b1000111001111000,
    0b1000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // <
    0b1000000000000000,
    0b1000000010000000,
    0b1000000111000000,
    0b1000001101100000,
    0b1000011000110000,
    0b1000010000010000,
    0b1000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // =
    0b1000011011000000,
    0b1000011011000000,
    0b1000011011000000,
    0b1000011011000000,
    0b1000011011000000,
    0b1000011011000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // >
    0b1000000000000000,
    0b1000010000010000,
    0b1000011000110000,
    0b1000001101100000,
    0b1000000111000000,
    0b1000000010000000,
    0b1000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // ?
    0b1000000000000000,
    0b1011000000000000,
    0b1111000000000000,
    0b1110000111101100,
    0b1110001111101100,
    0b1110011100000000,
    0b1111111000000000,
    0b1011110000000000,
    0b1000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // @
    0b1011100111111000,
    0b1111001111111100,
    0b1110001100001100,
    0b1110000111001100,
    0b1110000000001100,
    0b1111111111111100,
    0b1011111111111000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // A
    0b1011111111111100,
    0b1111111111111100,
    0b1110001100000000,
    0b1110001100000000,
    0b1110001100000000,
    0b1111111111111100,
    0b1011111111111100,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // B
    0b1111111111111100,
    0b1111111111111100,
    0b1110001100001100,
    0b1110001100001100,
    0b1110001100001100,
    0b1111111111111100,
    0b1011111011111000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // C
    0b1011111111111000,
    0b1111111111111100,
    0b1110000000001100,
    0b1110000000001100,
    0b1110000000001100,
    0b1111100000111100,
    0b1011100000111000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // D
    0b1111111111111100,
    0b1111111111111100,
    0b1110000000001100,
    0b1110000000001100,
    0b1110000000001100,
    0b1111111111111100,
    0b1011111111111000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // E
    0b1111111111111100,
    0b1111111111111100,
    0b1110001100001100,
    0b1110001100001100,
    0b1110001100001100,
    0b1110001100001100,
    0b1110000000001100,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // F
    0b1111111111111100,
    0b1111111111111100,
    0b1110001100000000,
    0b1110001100000000,
    0b1110001100000000,
    0b1110001100000000,
    0b1110000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // G
    0b1011111111111000,
    0b1111111111111100,
    0b1110000000001100,
    0b1110000000001100,
    0b1110000110001100,
    0b1111000111111100,
    0b1011000111111000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // H
    0b1111111111111100,
    0b1111111111111100,
    0b1000001100000000,
    0b1000001100000000,
    0b1000001100000000,
    0b1111111111111100,
    0b1111111111111100,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // I
    0b1111111111111100,
    0b1111111111111100,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // J
    0b1000000000111000,
    0b1000000000111100,
    0b1110000000001100,
    0b1110000000001100,
    0b1110000000001100,
    0b1111111111111100,
    0b1111111111111000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // K
    0b1111111111111100,
    0b1111111111111100,
    0b1000001111000000,
    0b1000011111100000,
    0b1000111001110000,
    0b1001110000111000,
    0b1011100000011100,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // L
    0b1111111111111100,
    0b1111111111111100,
    0b1000000000001100,
    0b1000000000001100,
    0b1000000000001100,
    0b1000000000001100,
    0b1000000000001100,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // M
    0b1111111111111100,
    0b1111111111111100,
    0b1011000000000000,
    0b1001100000000000,
    0b1000110000000000,
    0b1000110000000000,
    0b1001100000000000,
    0b1011000000000000,
    0b1111111111111100,
    0b1111111111111100,
  },
  {
    0b1000000000000000,  // N
    0b1111111111111100,
    0b1111111111111100,
    0b1001110000000000,
    0b1000111000000000,
    0b1000011100000000,
    0b1111111111111100,
    0b1111111111111100,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // O
    0b1011111111111000,
    0b1111111111111100,
    0b1110000000001100,
    0b1110000000001100,
    0b1110000000001100,
    0b1111111111111100,
    0b1011111111111000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // P
    0b1111111111111100,
    0b1111111111111100,
    0b1110001100000000,
    0b1110001100000000,
    0b1110001100000000,
    0b1111111100000000,
    0b1011111000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // Q
    0b1011111111111000,
    0b1111111111111100,
    0b1110000000001100,
    0b1110000001101100,
    0b1110000000111100,
    0b1111111111111100,
    0b1011111111111100,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // R
    0b1111111111111100,
    0b1111111111111100,
    0b1110001100000000,
    0b1110001100000000,
    0b1110001100000000,
    0b1111111111111100,
    0b1011111011111100,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // S
    0b1011111000001000,
    0b1111111100001100,
    0b1110001100001100,
    0b1110001100001100,
    0b1110001100001100,
    0b1110001111111100,
    0b1010000111111000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // T
    0b1110000000000000,
    0b1110000000000000,
    0b1110000000000000,
    0b1111111111111100,
    0b1111111111111100,
    0b1110000000000000,
    0b1110000000000000,
    0b1110000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // U
    0b1111111111111000,
    0b1111111111111100,
    0b1000000000001100,
    0b1000000000001100,
    0b1000000000001100,
    0b1111111111111100,
    0b1111111111111000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // V
    0b1111111111100000,
    0b1111111111110000,
    0b1000000000011000,
    0b1000000000001100,
    0b1000000000011000,
    0b1111111111110000,
    0b1111111111100000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // W
    0b1111111111110000,
    0b1111111111111000,
    0b1000000000011100,
    0b1000000000111000,
    0b1000000001110000,
    0b1000000001110000,
    0b1000000000111000,
    0b1000000000011100,
    0b1111111111111000,
    0b1111111111110000,
  },
  {
    0b1000000000000000,  // X
    0b1111000000011100,
    0b1111100000111100,
    0b1000110001100000,
    0b1000011111000000,
    0b1000011111000000,
    0b1000110001100000,
    0b1111100000111100,
    0b1111000000011100,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // Y
    0b1111110000000000,
    0b1111111000000000,
    0b1000001100000000,
    0b1000001111111100,
    0b1000001111111100,
    0b1000001100000000,
    0b1111111000000000,
    0b1111110000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // Z
    0b1110000001111100,
    0b1110000011111100,
    0b1110000111001100,
    0b1110001110001100,
    0b1110011100001100,
    0b1111111000001100,
    0b1111110000001100,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // [
    0b1111111111111100,
    0b1111111111111100,
    0b1110000000001100,
    0b1110000000001100,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // \
    0b1011000000000000,
    0b1011110000000000,
    0b1000111100000000,
    0b1000001111000000,
    0b1000000011110000,
    0b1000000000111100,
    0b1000000000001100,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // ]
    0b1110000000001100,
    0b1110000000001100,
    0b1111111111111100,
    0b1111111111111100,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // ^
    0b1000010000000000,
    0b1000110000000000,
    0b1001100000000000,
    0b1011000000000000,
    0b1001100000000000,
    0b1000110000000000,
    0b1000010000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // _
    0b1000000000000110,
    0b1000000000000110,
    0b1000000000000110,
    0b1000000000000110,
    0b1000000000000110,
    0b1000000000000110,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // `
    0b1000000000000000,
    0b1010000000000000,
    0b1011000000000000,
    0b1001000000000000,
    0b1000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // a
    0b1000010001111000,
    0b1000110011111100,
    0b1000110011001100,
    0b1000110011001100,
    0b1000111111111100,
    0b1000011111111100,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // b
    0b1111111111111100,
    0b1111111111111100,
    0b1000011000001100,
    0b1000011000001100,
    0b1000011111111100,
    0b1000001111111000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // c
    0b1000011111111000,
    0b1000111111111100,
    0b1000110000001100,
    0b1000110000001100,
    0b1000110000001100,
    0b1000011000011000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // d
    0b1000001111111000,
    0b1000011111111100,
    0b1000011000001100,
    0b1000011000001100,
    0b1111111111111100,
    0b1111111111111100,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // e
    0b1000011111111000,
    0b1000111111111100,
    0b1000110011001100,
    0b1000110011001100,
    0b1000111111001100,
    0b1000011111011000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // f
    0b1000001100000000,
    0b1011111111111100,
    0b1111111111111100,
    0b1110001100000000,
    0b1110001100000000,
    0b1110000000000000,
    0b1011000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // g
    0b1000011111001100,
    0b1000111111100110,
    0b1000110001100110,
    0b1000110001100110,
    0b1000111111111110,
    0b1000111111111100,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // h
    0b1111111111111100,
    0b1111111111111100,
    0b1000011000000000,
    0b1000011000000000,
    0b1000011111111100,
    0b1000001111111100,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // i
    0b1110111111111100,
    0b1110111111111100,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // j
    0b1000000000001100,
    0b1000000000000110,
    0b1000000000000110,
    0b1000000000000110,
    0b1110111111111110,
    0b1110111111111100,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // k
    0b1111111111111100,
    0b1111111111111100,
    0b1000000011000000,
    0b1000000111100000,
    0b1000001100110000,
    0b1000011000011000,
    0b1000110000001100,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // l
    0b1111111111111000,
    0b1111111111111100,
    0b1000000000001100,
    0b1000000000001100,
    0b1000000000001100,
    0b1000000000011000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // m
    0b1000011111111100,
    0b1000111111111100,
    0b1000110000000000,
    0b1000110000000000,
    0b1000011111111100,
    0b1000011111111100,
    0b1000110000000000,
    0b1000110000000000,
    0b1000111111111100,
    0b1000011111111100,
  },
  {
    0b1000000000000000,  // n
    0b1000111111111100,
    0b1000111111111100,
    0b1000110000000000,
    0b1000110000000000,
    0b1000111111111100,
    0b1000011111111100,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // o
    0b1000011111111000,
    0b1000111111111100,
    0b1000110000001100,
    0b1000110000001100,
    0b1000111111111100,
    0b1000011111111000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // p
    0b1000011111111111,
    0b1000111111111111,
    0b1000110001100000,
    0b1000110001100000,
    0b1000111111100000,
    0b1000011111000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // q
    0b1000011111000000,
    0b1000111111100000,
    0b1000110001100000,
    0b1000110001100000,
    0b1000111111111111,
    0b1000011111111110,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // r
    0b1000011111111100,
    0b1000111111111100,
    0b1000110000000000,
    0b1000110000000000,
    0b1000111000000000,
    0b1000011000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // s
    0b1000011110011000,
    0b1000111111001100,
    0b1000110011001100,
    0b1000110011001100,
    0b1000110011111100,
    0b1000011001111000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // t
    0b1000110000000000,
    0b1111111111111000,
    0b1111111111111100,
    0b1000110000001100,
    0b1000110000001100,
    0b1000000000001100,
    0b1000000000011000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // u
    0b1000111111111000,
    0b1000111111111100,
    0b1000000000001100,
    0b1000000000001100,
    0b1000111111111100,
    0b1000111111111000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // v
    0b1000111111000000,
    0b1000111111110000,
    0b1000000000111100,
    0b1000000000111100,
    0b1000111111110000,
    0b1000111111000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // w
    0b1000111111111000,
    0b1000111111111100,
    0b1000000000001100,
    0b1000000000001100,
    0b1000111111111000,
    0b1000111111111000,
    0b1000000000001100,
    0b1000000000001100,
    0b1000111111111100,
    0b1000111111111000,
  },
  {
    0b1000000000000000,  // x
    0b1000110000001100,
    0b1000111000011100,
    0b1000001111110000,
    0b1000001111110000,
    0b1000111000011100,
    0b1000110000001100,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // y
    0b1000111100000000,
    0b1000111111000000,
    0b1000000011111100,
    0b1000000011111100,
    0b1000111111000000,
    0b1000111100000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // z
    0b1000110000011100,
    0b1000110000111100,
    0b1000110011101100,
    0b1000110111001100,
    0b1000111100001100,
    0b1000111000001100,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // {
    0b1000000100000000,
    0b1001111111110000,
    0b1011111011111000,
    0b1111000000011100,
    0b1110000000001100,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // |
    0b1000000000000000,
    0b1111111111111100,
    0b1111111111111100,
    0b1000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // }
    0b1110000000001100,
    0b1111000000011100,
    0b1011111011111000,
    0b1001111111110000,
    0b1000000100000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // ~
    0b1001000000000000,
    0b1010000000000000,
    0b1010000000000000,
    0b1001000000000000,
    0b1000100000000000,
    0b1000100000000000,
    0b1001000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  },
  {
    0b1000000000000000,  // o degree symbol = ascii 0x7f = 127 dec.
    0b1000000000000000,
    0b1001100000000000,
    0b1010010000000000,
    0b1010010000000000,
    0b1001100000000000,
    0b1000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
  }
};