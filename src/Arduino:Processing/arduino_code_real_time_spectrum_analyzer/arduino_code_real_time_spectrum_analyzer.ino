/*
     Arduino - Processing Real Time Spectrum Analyzer

This program is intended output a FFT from a pc on a RGB matrix
The program is based on the adafruit RGB matrix library: https://learn.adafruit.com/32x16-32x32-rgb-led-matrix/
The FFT results in the complimentary processing code handles 64 bands so the code calls for 2 panels, but can be modified for only one easily
More information, including full parts list and videos of the final product can be seen on 12vtronix.com
Youtube video sample: https://www.youtube.com/watch?v=X35HbE7k3DA

           Created: 22nd Sep 2013 by Stephen Singh
     Last Modified: 10th May 2014 by Stephen Singh
     
     Variables with the <-O-> symbol indicates that it can be adjusted for the reason specified

*/



#include <avr/pgmspace.h>
#include <Adafruit_GFX.h>   // Core graphics library
#include <RGBmatrixPanel.h> // Hardware-specific library

#define CLK 11  // MUST be on PORTB!
#define LAT 9
#define OE  10
#define A   A0
#define B   A1
#define C   A2
#define D   A3
// Last parameter = 'true' enables double-buffering, for flicker-free,
// buttery smooth animation.  Note that NOTHING WILL SHOW ON THE DISPLAY
// until the first call to swapBuffers().  This is normal.
RGBmatrixPanel matrix(A, B, C, D, CLK, LAT, OE, true);



// <-O-> the values after "matrix.Color333" represent the RGB values with 7 being the brightest value for that particular colour

void lightcolumns(int rownum, int amplitude)
{
  if(rownum >= 0 && rownum < 32){
  
    if(amplitude>15)  // <-O-> set the threshold for the band to turn red
    {
    for( int y = 0; y < amplitude; y++){
    matrix.drawPixel(rownum, y+16, matrix.Color333(7, 0, 0));
    }
    for(int y = amplitude; y <16; y++)
    {
    matrix.drawPixel(rownum, y+16, matrix.Color333(0, 0, 0));  
    }
    }
    
    else if(amplitude>13) // <-O-> set the threshold for the band to turn yellow
    {
    for( int y = 0; y < amplitude; y++){
    matrix.drawPixel(rownum, y+16, matrix.Color333(4, 4, 0));
    }
    for(int y = amplitude; y < 16; y++)
    {
    matrix.drawPixel(rownum, y+16, matrix.Color333(0, 0, 0));  
    }
    }
    
    else if(amplitude>9) // <-O-> set the threshold for the band to turn green
    {
    for( int y = 0; y < amplitude; y++){
    matrix.drawPixel(rownum, y+16, matrix.Color333(0, 5, 0));
    }
    for(int y = amplitude; y < 16; y++)
    {
    matrix.drawPixel(rownum, y+16, matrix.Color333(0, 0, 0));  
    }
    } 
    
    else
    {
    for( int y = 0; y < amplitude; y++){
    matrix.drawPixel(rownum, y+16, matrix.Color333(0, 0, 7));
    }
    for(int y = amplitude; y < 16; y++)
    {
    matrix.drawPixel(rownum, y+16, matrix.Color333(0, 0, 0));  
    }
    } 
  }
  else
  {
    if(amplitude>15)  // <-O-> set the threshold for the band to turn red
    {
    for( int y = 0; y < amplitude; y++){
    matrix.drawPixel(rownum-32, y, matrix.Color333(7, 0, 0));
    }
    for(int y = amplitude; y <16; y++)
    {
    matrix.drawPixel(rownum-32, y, matrix.Color333(0, 0, 0));  
    }
    }
    
    else if(amplitude>13) // <-O-> set the threshold for the band to turn yellow
    {
    for( int y = 0; y < amplitude; y++){
    matrix.drawPixel(rownum-32, y, matrix.Color333(4, 4, 0));
    }
    for(int y = amplitude; y < 16; y++)
    {
    matrix.drawPixel(rownum-32, y, matrix.Color333(0, 0, 0));  
    }
    }
    
    else if(amplitude>9) // <-O-> set the threshold for the band to turn green
    {
    for( int y = 0; y < amplitude; y++){
    matrix.drawPixel(rownum-32, y, matrix.Color333(0, 5, 0));
    }
    for(int y = amplitude; y < 16; y++)
    {
    matrix.drawPixel(rownum-32, y, matrix.Color333(0, 0, 0));  
    }
    } 
    
    else
    {
    for( int y = 0; y < amplitude; y++){
    matrix.drawPixel(rownum-32, y, matrix.Color333(0, 0, 7));
    }
    for(int y = amplitude; y < 16; y++)
    {
    matrix.drawPixel(rownum-32, y, matrix.Color333(0, 0, 0));  
    }
    } 
  }
}

void setup() 
{ 
  matrix.begin();  
  Serial.begin(115200);
  delay(1000);
}





void loop() {


if(Serial.read() == ('M')) 
{
    int led1 = Serial.parseInt();    
    int led2 = Serial.parseInt(); 
    int led3 = Serial.parseInt();  
    int led4 = Serial.parseInt(); 
    int led5 = Serial.parseInt(); 
    int led6 = Serial.parseInt();  
    int led7 = Serial.parseInt(); 
    int led8 = Serial.parseInt(); 
    int led9 = Serial.parseInt();    
    int led10 = Serial.parseInt(); 
    int led11 = Serial.parseInt();  
    int led12 = Serial.parseInt(); 
    int led13 = Serial.parseInt(); 
    int led14 = Serial.parseInt();  
    int led15 = Serial.parseInt(); 
    int led16 = Serial.parseInt(); 
    int led17 = Serial.parseInt();    
    int led18 = Serial.parseInt(); 
    int led19 = Serial.parseInt();  
    int led20 = Serial.parseInt(); 
    int led21 = Serial.parseInt(); 
    int led22 = Serial.parseInt();  
    int led23 = Serial.parseInt(); 
    int led24 = Serial.parseInt(); 
    int led25 = Serial.parseInt();  
    int led26 = Serial.parseInt(); 
    int led27 = Serial.parseInt();  
    int led28 = Serial.parseInt(); 
    int led29 = Serial.parseInt(); 
    int led30 = Serial.parseInt();  
    int led31 = Serial.parseInt(); 
    int led32 = Serial.parseInt();
    int led33 = Serial.parseInt();    
    int led34 = Serial.parseInt(); 
    int led35 = Serial.parseInt();  
    int led36 = Serial.parseInt(); 
    int led37 = Serial.parseInt(); 
    int led38 = Serial.parseInt();  
    int led39 = Serial.parseInt(); 
    int led40 = Serial.parseInt(); 
    int led41 = Serial.parseInt();    
    int led42 = Serial.parseInt(); 
    int led43 = Serial.parseInt();  
    int led44 = Serial.parseInt(); 
    int led45 = Serial.parseInt(); 
    int led46 = Serial.parseInt();  
    int led47 = Serial.parseInt(); 
    int led48 = Serial.parseInt(); 
    int led49 = Serial.parseInt();    
    int led50 = Serial.parseInt(); 
    int led51 = Serial.parseInt();  
    int led52 = Serial.parseInt(); 
    int led53 = Serial.parseInt(); 
    int led54 = Serial.parseInt();  
    int led55 = Serial.parseInt(); 
    int led56 = Serial.parseInt(); 
    int led57 = Serial.parseInt();  
    int led58 = Serial.parseInt(); 
    int led59 = Serial.parseInt();  
    int led60 = Serial.parseInt(); 
    int led61 = Serial.parseInt(); 
    int led62 = Serial.parseInt();  
    int led63 = Serial.parseInt(); 
    int led64 = Serial.parseInt();  
    
    if (Serial.read() == '\n') 
    {     
      lightcolumns(63, led1);
      lightcolumns(62, led2);
      lightcolumns(61, led3);
      lightcolumns(60, led4);
      lightcolumns(59, led5);
      lightcolumns(58, led6);
      lightcolumns(57, led7);
      lightcolumns(56, led8);
      lightcolumns(55, led9);
      lightcolumns(54, led10);
      lightcolumns(53, led11);
      lightcolumns(52, led12);
      lightcolumns(51, led13);
      lightcolumns(50, led14);
      lightcolumns(49, led15);
      lightcolumns(48, led16);
      lightcolumns(47, led17);
      lightcolumns(46, led18);
      lightcolumns(45, led19);
      lightcolumns(44, led20);
      lightcolumns(43, led21);
      lightcolumns(42, led22);
      lightcolumns(41, led23);
      lightcolumns(40, led24);
      lightcolumns(39, led25);
      lightcolumns(38, led26);
      lightcolumns(37, led27);
      lightcolumns(36, led28);
      lightcolumns(35, led29);
      lightcolumns(34, led30);
      lightcolumns(33, led31);
      lightcolumns(32, led32);
      lightcolumns(31, led33);
      lightcolumns(30, led34);
      lightcolumns(29, led35);
      lightcolumns(28, led36);
      lightcolumns(27, led37);
      lightcolumns(26, led38);
      lightcolumns(25, led39);
      lightcolumns(24, led40);
      lightcolumns(23, led41);
      lightcolumns(22, led42);
      lightcolumns(21, led43);
      lightcolumns(20, led44);
      lightcolumns(19, led45);
      lightcolumns(18, led46);
      lightcolumns(17, led47);
      lightcolumns(16, led48);
      lightcolumns(15, led49);
      lightcolumns(14, led50);
      lightcolumns(13, led51);
      lightcolumns(12, led52);
      lightcolumns(11, led53);
      lightcolumns(10, led54);
      lightcolumns(9, led55);
      lightcolumns(8, led56);
      lightcolumns(7, led57);
      lightcolumns(6, led58);
      lightcolumns(5, led59);
      lightcolumns(4, led60);
      lightcolumns(3, led61);
      lightcolumns(2, led62);
      lightcolumns(1, led63);
      lightcolumns(0, led64);

      matrix.swapBuffers(false);
    }
  }
}
