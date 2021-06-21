class GameSaver(object):

    def load(self, file_name, *argv):
        """
        Reads file. If the file dodn't exist, creates a new one on which writes
        one argv per line. Returns string of file content.
        """
        self.name = file_name
        try:
            fi = open(self.name, 'r')
        except FileNotFoundError:
            print("Game hasn't been played before.")
            print("Starting new game.")
            # Creating file with starting game value
            # So following process is same for new and already started game
            fi = open(self.name, 'w+')
            arg_list = []
            for arg in argv:
                fi.write(f"{arg}\n")
                arg_list.append(str(arg))
                print(arg_list)
            position = '\n'.join(arg_list)
            print(position)
        else:
            print("Game was already started, loading.")
            position = fi.read()
        finally:
            print(position)
            fi.close()
            return position

    def save(self, file_name, *argv):
        """
        On file writes argv. Each for own line.
        """
        self.name = file_name
        f = open(self.name, 'w')
        for arg in argv:
            f.write(f"{arg}\n")
        f.close()