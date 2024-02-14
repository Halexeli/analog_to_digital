#include <SDL.h>
#include <math.h>

#include "rotations.h"
/*
  This code shows how to calculate a rotation of a SDL_Surface.

  Copyright (C) 2006 Florent Humbert http://www.developpez.net/forums/member.php?u=103584

  This program is free software; you can redistribute it and/or
  modify it under the terms of the GNU General Public License
  as published by the Free Software Foundation; either version 2
  of the License, or (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program; if not, write to the Free Software
  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
*/

/*permet de d�terminer la valeur d'un pixel au position x,y*/
static Uint32 SDL_LirePixel(SDL_Surface* surface, int x, int y);
/*permet d'�crire un pixel au position x,y*/
static void SDL_EcrirePixel(SDL_Surface* surface, int x, int y, Uint32 pixel);

/*permet de d�terminer la valeur d'un pixel au position x,y*/
inline Uint32 SDL_LirePixel(SDL_Surface* surface, int x, int y)
{
  int bpp = surface->format->BytesPerPixel;

  Uint8 *p = (Uint8 *)surface->pixels + y * surface->pitch + x * bpp;

  switch(bpp)
  {
             case 1:
                  return *p;
             case 2:
                  return *(Uint16 *)p;
             case 3:
                 if(SDL_BYTEORDER == SDL_BIG_ENDIAN)
                     return p[0] << 16 | p[1] << 8 | p[2];
                 else
                     return p[0] | p[1] << 8 | p[2] << 16;
             case 4:


                  return *(Uint32 *)p;
             default:
                  return 0;
  } 
       
}


/*permet d'�crire un pixel au position x,y*/
inline void SDL_EcrirePixel(SDL_Surface* surface, int x, int y, Uint32 pixel)
{
    int bpp = surface->format->BytesPerPixel; 
    Uint8 *p = (Uint8 *)surface->pixels + y * surface->pitch + x * bpp; 
  
  
    switch(bpp) { 
    case 1: 
        *p = pixel; 
        break; 
  
    case 2: 
        *(Uint16 *)p = pixel; 
        break; 
  
    case 3: 
        if(SDL_BYTEORDER == SDL_BIG_ENDIAN) { 
            p[0] = (pixel >> 16) & 0xff; 
            p[1] = (pixel >> 8) & 0xff; 
            p[2] = pixel & 0xff; 
        } else { 
            p[0] = pixel & 0xff; 
            p[1] = (pixel >> 8) & 0xff; 
            p[2] = (pixel >> 16) & 0xff; 
        } 
        break; 
  
    case 4: 

        *(Uint32 *)p = pixel; 
        break; 
    }  
  
}

/*effectue une rotation centrale d'angle en degr�, alloue automatiquement la m�moire*/
SDL_Surface* SDL_RotationCentral(SDL_Surface* origine, float angle)
{
 SDL_Surface* destination;
 int i;
 int j;
 Uint32 couleur;
 int mx, my;
 int bx, by;
 float angle_radian;

/* d�termine la valeur en radian de l'angle*/
 angle_radian = -angle * M_PI / 180.0;

/* 
 * alloue la m�moire � l'espace de destination, attention, 
 * la surface est de m�me taille
 */
 destination = SDL_CreateRGBSurface(SDL_HWSURFACE, origine->w, origine->h, origine->format->BitsPerPixel,
			origine->format->Rmask, origine->format->Gmask, origine->format->Bmask, origine->format->Amask);

 /*on v�rifie que la m�moire a �t� allou�e*/
 if(destination==NULL)
  return NULL;

/* pour simplifier les notations*/
 mx = origine->w/2;
 my = origine->h/2;

 for(j=0;j<origine->h;j++)
  for(i=0;i<origine->w;i++)
  {
/* on d�termine la valeur de pixel qui correspond le mieux pour la position
 * i,j de la surface de destination */

/* on d�termine la meilleure position sur la surface d'origine en appliquant
 * une matrice de rotation inverse
 */
   bx = (int) (cos(angle_radian) * (i-mx) + sin(angle_radian) * (j-my)) + mx;
   by = (int) (-sin(angle_radian) * (i-mx) + cos(angle_radian) * (j-my)) + my;
   /* on v�rifie que l'on ne sort pas des bords*/
   if (bx>=0 && bx< origine->w && by>=0 && by< origine->h)
   {
     couleur = SDL_LirePixel(origine, bx, by);
     SDL_EcrirePixel(destination, i, j, couleur);
   }
  }

return destination;
}

/*effectue une rotation centrale, alloue automatiquement la m�moire*/
SDL_Surface* SDL_RotationCentralN(SDL_Surface* origine, float angle)
{
 SDL_Surface* destination;
 int i;
 int j;
 Uint32 couleur;
 int mx, my, mxdest, mydest;
 int bx, by;
 float angle_radian;
 float tcos;
 float tsin;
 double largeurdest;
 double hauteurdest;
 
/* d�termine la valeur en radian de l'angle*/
 angle_radian = -angle * M_PI / 180.0;

/*pour �viter pleins d'appel, on stocke les valeurs*/
 tcos = cos(angle_radian);
 tsin = sin(angle_radian);
 
/*calcul de la taille de l'image de destination*/
 largeurdest=   ceil(origine->w * fabs(tcos) + origine->h * fabs(tsin)),
 hauteurdest=   ceil( origine->w * fabs(tsin) + origine->h * fabs(tcos)),


/* 
 * alloue la m�moire � l'espace de destination, attention, 
 * la surface est de m�me taille
 */
 destination = SDL_CreateRGBSurface(SDL_HWSURFACE, largeurdest, hauteurdest, origine->format->BitsPerPixel,
			origine->format->Rmask, origine->format->Gmask, origine->format->Bmask, origine->format->Amask);

 /*on v�rifie que la m�moire a �t� allou�e*/
 if(destination==NULL)
  return NULL;
 
 /*calcul du centre des images*/
 mxdest = destination->w/2.;
 mydest = destination->h/2.;
 mx = origine->w/2.;
 my = origine->h/2.;
 
 for(j=0;j<destination->h;j++)
  for(i=0;i<destination->w;i++)
  {
/* on d�termine la valeur de pixel qui correspond le mieux pour la position
 * i,j de la surface de destination */

/* on d�termine la meilleure position sur la surface d'origine en appliquant
 * une matrice de rotation inverse
 */

   bx = (ceil (tcos * (i-mxdest) + tsin * (j-mydest) + mx));
   by = (ceil (-tsin * (i-mxdest) + tcos * (j-mydest) + my));
   /* on v�rifie que l'on ne sort pas des bords*/
   if (bx>=0 && bx< origine->w && by>=0 && by< origine->h)
   {
     couleur = SDL_LirePixel(origine, bx, by);
     SDL_EcrirePixel(destination, i, j, couleur);
   }
 }

return destination;
}
