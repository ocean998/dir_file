import time

def timer(func):
   print( 'timer(func) begin start !' )
   def runtime():
      print( 'runtime() begin start !' )
      start_t = time.time( )
      func( )
      stop_t = time.time( )
      print( 'runing second : %s' % (stop_t - start_t) )
      print( 'runtime()  end !\n' )

   print( 'timer(func)  end !\n' )
   return runtime

@timer
def dcrt():
   print('dcrt() begin sleep !')
   time.sleep(2)
   print( 'dcrt() wakeup !\n' )

# dcrt()