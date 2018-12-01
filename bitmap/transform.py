import cmd
import sys
import os
import bitmap


class BitmapManipulator(cmd.Cmd):
    intro = 'Welcome to the bitmap manipulator.   Type help or ? to list commands.\n'
    prompt = '> '

    @staticmethod
    def do_get_headers(source):
        """
        To use this type 'get_headers' followed by the file location's source.

        get_headers <source>

        Returns a line-item response of the file's header data.
        """
        splitted = source.split()
        if len(splitted) > 1:
            print('invalid number of arguments')
            return
        if source == '':
            print('no file specified')
            return
        try:
            to_read = bitmap.Bitmap.read_file(source)
            print(f'Here are the headers for {source}:')
            print(to_read.get_headers())
        except FileNotFoundError:
            print('file cannot be read')

    def do_transform(self, arg):
        """
        To use this type in 'transform' followed by
        the original file location and the new file location
        and the type of change you would like to do.

        transform <original> <new> <transform>

        Creates a new file at 'new' location with the provided 'transform' applied to the new file.
        """
        # TODO: Complete these CLI methods for performing described actions
        splitted = arg.split()
        if len(splitted) != 3:
            print('invalid number of arguments')
            return
        ext = splitted[1].split('.')
        if len(ext) == 1:
            print('no extension specified')
            return
        elif ext[1] != 'bmp':
            print('wrong extension')
            return
        try:
            to_read = bitmap.Bitmap.read_file(splitted[0])
        except FileNotFoundError:
            print('No such file!')
            return

        if splitted[2] == 'tint_red':
            to_read.tint_color('red')
        elif splitted[2] == 'tint_blue':
            to_read.tint_color('blue')
        elif splitted[2] == 'tint_green':
            to_read.tint_color('green')
        elif splitted[2] == 'lighten':
            to_read.lighten_darken('light')
        elif splitted[2] == 'darken':
            to_read.lighten_darken('dark')
        elif splitted[2] == 'invert':
            to_read.invert()
        elif splitted[2] == 'cave':
            to_read.the_cave()
        else:
            print('invalid transform')
            return

        to_read.write_file(splitted[1])
        print(f'{splitted[0]} has been transformed and can be found at {os.getcwd()}/{splitted[1]}')


    @staticmethod
    def do_exit(args):
        """
        To use this type in 'exit' and the CLI tool will cleanly exit the running application.
        """
        sys.exit()


if __name__ == '__main__':
    BitmapManipulator().cmdloop()


