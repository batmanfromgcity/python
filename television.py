class Television:

    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL



    def power(self) -> None:
        '''This method toggles the power on and off'''
        self.__status = not self.__status

    def mute(self) -> None:
        '''This method toggles the mute on and off'''
        if self.__status == True:
            self.__muted = not self.__muted


    def channel_up(self) -> None:
        '''This method increases the channel by 1'''
        if self.__status == True:
            if self.__channel < self.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = self.MIN_CHANNEL


    def channel_down(self) -> None:
        '''This method decreases the channel by 1'''
        if self.__status == True:
            if self.__channel > self.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = self.MAX_CHANNEL


    def volume_up(self) -> None:
        '''This method increases the volume by 1'''
        if self.__status == True:
            self.__muted = False
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1


    def volume_down(self) -> None:
        '''This method decreases the volume by 1'''
        if self.__status == True:
            self.__muted = False
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1



    def __str__(self) -> str:
        '''This method returns the string representation of the tv object'''
        if self.__muted == True:
            return "Power = {}, Channel = {}, Volume = {}".format(self.__status, self.__channel, Television.MIN_VOLUME)
        else:
            return "Power = {}, Channel = {}, Volume = {}".format(self.__status, self.__channel, self.__volume)
    
    