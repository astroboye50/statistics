# IS EVEN
def mod2( xln ):

  if( xln % 2 ) == 0:                    # check modulus(2) remainder
     return True                         # is even

  return False                           # is odd


# CALCULATE TOTAL
def total( run, ttl ):                   # for (p)n/(x^1, x^2, ... x^n) yield i

  for i in run:                          # iterate each element of list
     ttl += i                            # running total

  return ttl


# (X)Bar, Mew ( avg on set(n) or subset(N) xln or Xln )
def mxbar( ttl, xln, xbr ):

  xbr  =  float( float(ttl) / float(xln) )

  return xbr


# MEDIAN OF SET
def median( run, xln, mde, sum=None ):

  index  =  xln // 2

  if( sum ):
     return sorted( run )[index]

  # IDO: no mathlib, bubble sort
  return sum( sorted( run )[index -1:index + 1] ) / 2


# MODE OF SET
# IDO: no lazy init return
def mode( run ):

  # IDO: no imports
  from collections import Counter

  c  =  Counter( run )

  return [k for k, v in c.items() if v == c.most_common(1)[0][1]]
  

# DIFFEREMCE (funny U), sigma (onion)
# INPUT: sample, average
# OUTPUT: relative difference (f)
def sdif( run, avg, dif ):
  
  avg  =  float( avg )
  dif  =  []                               # redundant clear ( LIFO /xor/ FIFO )

  for r in run:
     r  =  float( r )                      # sample element
     e  =  float( r - avg )                # variance

     dif.append( e )

  return dif


# STANDARD VARIANCE  SIGMA_SQUARED (param)
def svar( dif, svr ):

  i    =  0                                # iterate count
  svr  =  0.0                              # running total
  
  for e in dif:
     e     =  float( e )
     svr   =  float( svr + (e * e) )         # total difference
     i     =  i + 1

  print( svr )
  print( i )
  svr = float( svr / float(i) )            # average variance (sigma^2)

  return svr


# RETURN SQUARE ROOT
def quadrt( bse, sqt ):
  from math import sqrt                    # IDO: prime factorization
  
  bse  =  float( bse )                     # parameter
  sqt  =  float( sqrt( bse ) )             # square root

  return sqt


# STANDARD DEVIATION (SIGMA)_onion         # sigma
def sdiv( svr, sdv ):
  
   sdv = quadrt( svr, sdv )                # square root of variance

   return sdv


# ALL THE THING
def stats( run ):
  # if its not bon, its crap

  dif  =  []                                  # difference
  mod  =  []                                  # mode

  var  =  0.0                                 # sandard variance
  avg  =  0.0                                 # mean( average ) of set
  ttl  =  0.0                                 # total sum of set
  xbr  =  0.0                                 # mean of set
  svr  =  0.0                                 # standard variance
  sdv  =  0.0                                 # standard deviation

  mde  =  None                                # median
  
  xln  =  len( run )                          # lenth of set elements
  Xln  =  xln - 1                             # minus one for X and N sub deviation

  ttl  =  total( run, ttl )                   # solved sum
  xbr  =  mxbar( ttl, xln, xbr )              # solved mean

  dif  =  sdif( run, xbr, dif )               # difference
  
  svr  =  float( svar( dif, svr ) )           # standard variance
  sdv  =  float( sdiv( svr, sdv ) )           # standard deviation


  # median: sum is required to compute index offset with odd number (n)
  if mod2( xln ):                             # is even (n)
     mde  =  median( run, xln, mde, sum )
  
  else:
     mde  =  median( run, xln, mde )          # is odd (n)

  mod  =  mode( run )                         # solved mode


  # PRINT ALL THE THINGS
  print( "SET:\t%s\n"                        %  str( run ) )                # if its not assembly its c
  print( "SUM:\t%d\n"                        %  ttl )                       # SUM
  print( "LENGTH SET:\t%d"                   %  xln )                       # LEN
  print( "(X)BAR:\t%s\n"                     %  '{:3.2f}'.format( xbr ) )   # XBAR (AVERAGE)
  print( "MEDIAN:\t%s\n"                     %  '{:3.2f}'.format( mde ) )   # MEDIAN
  print( "MODE:\t%s\n"                       %  str( mod ) )                # MODE
  print( "DIFFERENCE:\t%s\n"                 %  str( dif ) )                # STANDARD DIFFERENCE (STD is a c++ reserved function)
  print( "STANDARD VARIANCE SIGMA^2:\t%s\n"  %  '{:3.2f}'.format( svr ) )   # STANDARD VARIANCE
  print( "STANDARD DEVIATION SIGMA:\t%s\n"   %  '{:3.2f}'.format( sdv ) )   # STANDARD DEVIATION


# MAIN
def zing():
  run = [ 0, 5, 13, 7, 6, 5, 9,  7 ]
  stats( run )


# RUNTIME LINK
if __name__ == "__main__":
  zing()
