#funny child targeting system
import photonlibpy.photonCamera
from photonlibpy.photonTrackedTarget import PhotonTrackedTarget



class FunnyChildTargetingSystem():
    def __init__(self):
        self.camera = photonlibpy.photonCamera.PhotonCamera("child_detector")
        self.camera.setDriverMode(False)
        pass
    def getResults(self):
        results = self.camera.getLatestResult().getTargets()
        largest_area = 0
        returned_target = PhotonTrackedTarget()
        if len(results) == 0:
            pass
        for i in results:
            if i.getArea() > largest_area:
                returned_target = i
                largest_area = i.getArea()
                
        return returned_target
    
    def createCameraFeed(self):
        """
        only use this if your using the manual drive mode
        :return:
        """
        self.camera.setDriverMode(True)
    
    
        
        
            
       
    
    