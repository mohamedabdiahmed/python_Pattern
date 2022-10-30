class Singeleton_Python :
    _instance_=None
    
def _init_(Self):
    #this is constructor;
    if Singeleton_Python._instance_isNone:
        Singeleton_Python._instance_=Self
    else:
     raiseException("we cannot create another class")

    @staticmethod
    def get_instance():
        #we define the static method to fetch instance 
        if not Singeleton_Python._instance_:
            Singeleton_Python()
        return Singeleton_Python._instance_

    #creating an object of above defined class.
    gover= Singeleton_Python()
    print(gover)

    same_gover= Singeleton_Python.get_instance()
    print(same_gover)


    another_gover= Singeleton_Python()
    print(another_gover)

    new_gover = Singeleton_Python()
    print(new_gover)

    print("Hello World Python3...")

# Double Checked Locking singleton pattern   
import threading   
class Single_Checked(object):   
  
   # resources shared by each and every   
   # instance   
  
   __single_acq_lock = threading.Lock()   
   __singleton_instance = None  
  
   # define the classmethod   
   @classmethod  
   def instance(cls):   
  
      # check for the singleton instance   
      if not cls.__singleton_instance:   
         with cls.__single_acq_lock:   
            if not cls.__singleton_instance:   
               cls.__singleton_instance = cls()   
  
      # return the singleton instance   
      return cls.__singleton_instance   
  
# main method   
if __name__ == '__main__':   
  
   # create class A   
   class A(Single_Checked):   
      pass  
  
   # create class B  
   class B(Single_Checked):   
      pass  
  
   X1, X2 = A.instance(), A.instance()   
   Y1, Y2 = B.instance(), B.instance()   
  
   assert X1 is not Y1   
   assert X1 is X2   
   assert Y1 is Y2   
  
   print('X1 : ', X1)   
   print('X2 : ', X2)   
   print('Y1 : ', Y1)   
   print('Y2 : ', Y2)  