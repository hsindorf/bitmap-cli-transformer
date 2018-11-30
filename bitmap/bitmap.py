import struct
import random
import binascii


class Bitmap(object):
    def __init__(self, file_data):
        """Initialization method for Bitmap instance.
        Provides itemized data related to consumed Bitmap file through the use
        of a MemoryView object.
        """
        self.source = bytearray(file_data)
        self.memory_view = memoryview(self.source)

        self.offset = struct.unpack('I', self.memory_view[10:14].tobytes())[0]
        self.color_table = self.memory_view[54:self.offset]
        self.pixel_array = self.memory_view[self.offset:]

    @classmethod
    def read_file(cls, origin):
        """Class Method which consumes a file path as input, and returns a
        Bitmap instance.
        """
        # TOTEST: Complete this method for consuming a file from the file system
        # and creating a BMP instance (cls).
        try:
            with open(origin, 'rb') as binary_data:
                opened_data = binary_data.read()
                new_binary = Bitmap(opened_data)
                return new_binary
        except FileNotFoundError:
            raise FileNotFoundError('File not found!')
        except IOError:
            raise IOError('There was an issue reading the file')

    def write_file(self, target):
        """Instance Method which accepts a target file path and writes the
        instance source data to target path.
        """
        # TOTEST: Complete this method for writing a file from to the file
        # system from the BMP instance (self).

        if target == '':
            raise ValueError('Target filename cannot be blank')

        with open(target, 'wb') as target_file:
            try:
                target_file.write(self.source)
            except IOError:
                print('There was an issue writing to the file')

    def get_headers(self):
        """Instance Method which provides instance source data as readable
        output to std out.
        """
        import struct as s
        result = f'''
            Type: {self.memory_view[0:2].tobytes().decode()}
            Size: {s.unpack('I', self.memory_view[2:6].tobytes())[0]}
            Reserved 1: {s.unpack('H', self.memory_view[6:8].tobytes())[0]}
            Reserved 2: {s.unpack('H', self.memory_view[8:10].tobytes())[0]}
            Offset: {s.unpack('I', self.memory_view[10:14].tobytes())[0]}
            DIB Header Size: {s.unpack('I', self.memory_view[14:18].tobytes())[0]}
            Width: {s.unpack('I', self.memory_view[18:22].tobytes())[0]}
            Height: {s.unpack('I', self.memory_view[22:26].tobytes())[0]}
            Colour Planes: {s.unpack('H', self.memory_view[26:28].tobytes())[0]}
            Bits per Pixel: {s.unpack('H', self.memory_view[28:30].tobytes())[0]}
            Compression Method: {s.unpack('I', self.memory_view[30:34].tobytes())[0]}
            Raw Image Size: {s.unpack('I', self.memory_view[34:38].tobytes())[0]}
            Horizontal Resolution: {s.unpack('I', self.memory_view[38:42].tobytes())[0]}
            Vertical Resolution: {s.unpack('I', self.memory_view[42:46].tobytes())[0]}
            Number of Colours: {s.unpack('I', self.memory_view[46:50].tobytes())[0]}
            Important Colours: {s.unpack('I', self.memory_view[50:54].tobytes())[0]}
        '''
        return result

    # TODO: Write your instance methods for transformations here as part of the
    #  Bitmap class.

    def tint_color(self, input_color):
        """
        Instance method that makes the bitmap photo turn red

        input:
            input_color: string matching color to turn photo
        output: no return, saves modified photo to machine
        """
        if input_color == 'red':
            input_color = 3
        if input_color == 'blue':
            input_color = 1
        if input_color == 'green':
            input_color = 2

        for i in range(len(self.color_table)):
            if self.color_table[i] == 0 and i < len(self.color_table) - input_color:
                color = self.color_table[i + input_color] + 100
                if color > 255:
                    color = 255

                self.color_table[i + input_color] = color

    def lighten_darken(self, light_or_dark):
        """
        Lightens or darkens the bitmap image depending on keyword passed in

        input:
            light_or_dark: string, which to turn the photo
        output: no return, saves modified photo to machine
        """

        if light_or_dark == 'light':
            light_or_dark = 30
        else:
            light_or_dark = -30

        for i in range(len(self.color_table)):
            if self.color_table[i] != 0:
                color = self.color_table[i] + light_or_dark

                if color > 255:
                    color = 255

                if color <= 1:
                    color = 1

                self.color_table[i] = color

    def invert(self):
        """
        Inverts the bitmap image - this only does black/white.
        It will turns the whites into blacks and vice versa.

        No input/output
        """

        for i in range(len(self.pixel_array)):
            color = abs(255 - self.pixel_array[i])

            self.pixel_array[i] = color

    def the_cave(self):
        """
        Does a vignette-like filter

        No input/output
        """

        for i in range(len(self.pixel_array)):
            x = i % 256
            y = i // 256

            position = abs(128 - y) + abs(128 - x)

            color = self.pixel_array[i] - int((position**2 * .006))

            if color <= 1:
                color = 2

            if color >= 255:
                color = 255

            self.pixel_array[i] = color



if __name__ == "__main__":
    my_bitmap = Bitmap.read_file('bmp.bmp')

    # print(my_bitmap.get_headers())

    # my_bitmap.lighten_darken('dark')
    # my_bitmap.invert()
    # my_bitmap.tint_color('red')
    # my_bitmap.the_cave()

    my_bitmap.write_file('test2.bmp')
