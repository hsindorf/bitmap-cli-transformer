import cmd
import sys
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
        # TODO: Complete these CLI methods for performing described actions
        to_read = bitmap.Bitmap.read_file(source)
        print(to_read.get_headers())


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

        to_read = bitmap.Bitmap.read_file(splitted[0])
        if splitted[2] == 'tint_red':
            to_read.tint_color('red')
        if splitted[2] == 'tint_blue':
            to_read.tint_color('blue')
        if splitted[2] == 'tint_green':
            to_read.tint_color('green')
        if splitted[2] == 'lighten':
            to_read.lighten_darken('light')
        if splitted[2] == 'darken':
            to_read.lighten_darken('dark')
        if splitted[2] == 'invert':
            to_read.invert()
        if splitted[2] == 'cave':
            to_read.the_cave()

        to_read.write_file(splitted[1])


    @staticmethod
    def do_exit(args):
        """
        To use this type in 'exit' and the CLI tool will cleanly exit the running application.
        """
        sys.exit()


if __name__ == '__main__':
    BitmapManipulator().cmdloop()


