from math import sin, cos, sqrt, atan2, radians


class gpsdistance():


    def get_2distance(self, lat1, lon1, lat2, lon2):

        R = 6373.0

        lat1 = radians(lat1)
        lon1 = radians(lon1)
        lat2 = radians(lat2)
        lon2 = radians(lon2)

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = R * c

        # output km
        return distance


    def get_3distance(self,lat1,lon1,alt1,lat2,lon2,alt2):


        # 畢達哥拉斯
        alt_diff = alt2 - alt1
        _2distance = self.get_2distance(lat1,lon1,lat2,lon2)
        distance = sqrt((_2distance * _2distance) + (alt_diff * alt_diff))

        return distance

if __name__ == '__main__':
    pass
