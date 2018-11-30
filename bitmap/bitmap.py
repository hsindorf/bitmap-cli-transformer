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

    def make_red(self):
        """Instance method that makes the bitmap photo turn red"""
        for i in range(len(self.color_table)):
            # print(self.color_table[i])
            # color = binascii.hexlify(self.pixel_array[i].to_bytes(4, byteorder='big'))
            if self.color_table[i] == 0 and i != len(self.color_table) - 1:
                color = self.color_table[i + 3] + 100
                if color > 255:
                    color = 255

                self.color_table[i + 3] = color




    def lighten(self):
        """Instance method that lights the bitmap photo"""
        for i in range(65535):
            color = self.pixel_array[i] + 100

            if color > 255:
                color = 255

            self.pixel_array[i] = color


if __name__ == "__main__":
    my_bitmap = Bitmap.read_file('bmp.bmp')

    # print(my_bitmap.get_headers())

    # my_bitmap.lighten()
    my_bitmap.make_red()

    my_bitmap.write_file('test2.bmp')
