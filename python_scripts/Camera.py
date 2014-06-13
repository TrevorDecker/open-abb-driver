import pygame.camera
import pygame.image


class Camera:
    cam = ""
    def __init__(self,camNum):
        pygame.camera.init();
        self.cam = pygame.camera.Camera(pygame.camera.list_cameras()[camNum]);

    def __del__(self):
        pygame.camera.quit()

    def startCam(self):
        self.cam.start()

    def stopCam(self):
        self.cam.stop()

    def captureImage(self,fileName):
        img = self.cam.get_image()
        pygame.image.save(img,fileName)
