#!/usr/bin/python3
"""The `console` module supplies a class `HBNBCommand`
that sub-classes the `Cmd` class which helps in the implementation
of a custom CLI (command line interpreter) for our AirBnb console
project."""


import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Defines a class `HBNBCommand` that inherits
    from `Cmd` class"""
    prompt = "(hbnb) "
    cls = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review
    }

    def do_quit(self, line):
        """\nQuits the shell"""
        return True

    def help_quit(self):
        """\nDisplays help text for quit command."""
        print("Quit command to exit the program\n")

    def do_EOF(self, line):
        """\nQuits the shell on EOF."""
        return True

    def help_EOF(self):
        """\nDisplays help text for EOF command."""
        print("Quits the shell on EOF character\n")

    def emptyline(self):
        """\nEnsures last command is not repeated on empty command."""
        pass

    def do_create(self, line):
        """\nCreates a new instance of `BaseModel` saves it to JSON file.
        Usage: create <classname>
        """
        line = line.split()
        if len(line) < 1:
            print("** class name missing **")
        elif line[0] not in HBNBCommand.cls:
            print("** class doesn't exist **")
        else:
            for cls_name in HBNBCommand.cls:
                if cls_name == line[0]:
                    obj = HBNBCommand.cls[cls_name]()
            print(obj.id)
            storage.save()

    def do_show(self, line):
        """\nPrints the string representation of an instance
        based on classname and id.
        Usage: show <classname> <id>
        """
        line = line.split()
        if len(line) < 1:
            print("** class name missing **")
        elif len(line) == 1:
            print("** instance id missing **")
        elif line[0] not in HBNBCommand.cls:
            print("** class doesn't exist **")
        else:
            try:
                li = line[0], line[1]
                obj_id = ".".join(li)
                obj_dict = storage.all()
                try:
                    print(obj_dict[obj_id])
                except KeyError:
                    print("** no instance found **")
            except IndexError:
                pass

    def do_destroy(self, line):
        """\nDeletes an instance based on classname and id.
        Usage: destroy <classname> <id>
        """
        line = line.split()
        if len(line) < 1:
            print("** class name missing **")
        elif len(line) == 1:
            print("** instance id missing **")
        elif line[0] not in HBNBCommand.cls:
            print("** class doesn't exist **")
        else:
            try:
                obj_id = line[0] + "." + line[1]
                obj_dict = storage.all()
                try:
                    del (obj_dict[obj_id])
                    storage.save()
                except KeyError:
                    print("** no instance found **")
            except IndexError:
                pass

    def do_all(self, line):
        """\nPrints the string representation of all instances
        based or not classname.
        Usage: all <classname> or all
        """
        storage.reload()
        line = line.split()
        obj_dict = storage.all()
        obj_li = []
        if len(line) == 0:
            for obj in obj_dict.values():
                obj_li.append(obj.__str__())
            print(obj_li)
        elif len(line) >= 1 and line[0] in HBNBCommand.cls:
            for key, obj in obj_dict.items():
                if key.startswith(line[0] + "."):
                    obj_li.append(obj.__str__())
            print(obj_li)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """\nUpdates an attributes value
        Usage: update <classname> <id> <name> <value>"""
        storage.reload()
        line = line.split()
        obj_dict = storage.all()
        if len(line) < 1:
            print("** class name missing **")
        elif len(line) == 1:
            print("** instance id missing **")
        elif len(line) == 2:
            print("** attribute name missing **")
        elif len(line) == 3:
            print("** value missing **")
        else:
            if line[0] in HBNBCommand.cls:
                key = line[0] + "." + line[1]
                if key not in obj_dict.keys():
                    print("** no instance found **")
                else:
                    try:
                        attr_val_cast = type(eval(line[3]))
                        attr_val = line[3].strip("'")
                        attr_val = line[3].strip('"')
                        setattr(obj_dict[key], line[2],
                                attr_val_cast(attr_val))
                        obj_dict[key].save()
                    except (KeyError, AttributeError):
                        pass
            else:
                print("** class doesn't exist **")

    def default(self, line):
        """Runs commands who's method are not explicitly
        defined in the class"""
        if "." in line:
            try:
                s_line = line.replace(".", " ").split()
                s_l = line.replace(".", "*").split("*")

                if s_line[0] in HBNBCommand.cls and s_line[1] == "all()":
                    self.do_all(s_line[0])
                elif s_line[0] in HBNBCommand.cls and s_line[1] == "count()":
                    obj_dict = storage.all()
                    count = 0
                    for key in obj_dict.keys():
                        if key.startswith(s_line[0] + "."):
                            count += 1
                    print(count)
                else:
                    if (s_line[0] in HBNBCommand.cls and (
                            s_line[1].startswith('show("') and
                            s_line[1].endswith('")'))):
                        i_d = s_line[1].replace("(", " ").replace(
                            ")", "").replace('"', "").split()
                        i_d = i_d[1]
                        obj_id = s_line[0] + " " + i_d
                        self.do_show(obj_id)

                    elif (s_line[0] in HBNBCommand.cls and (
                            s_line[1].startswith('destroy("') and
                            s_line[1].endswith('")'))):
                        i_d = s_line[1].replace("(", " ").replace(
                            ")", "").replace('"', "").split()
                        i_d = i_d[1]
                        obj_id = s_line[0] + " " + i_d
                        self.do_destroy(obj_id)

                    elif (s_l[0]) in HBNBCommand.cls and (
                            s_l[1].startswith('update("') and
                            s_l[1].endswith(')')):
                        storage.reload()
                        cls_name = s_l[0]
                        s_l = s_l[1].replace("(", " ").replace(")", "")
                        s_l = s_l.replace('"', "").replace(",", "").split()
                        args = cls_name + " " + \
                            s_l[1] + " " + s_l[2] + " " + s_l[3]
                        try:
                            self.do_update(args)
                            storage.save()
                        except (AttributeError, NameError):
                            obj_dict = storage.all()
                            obj_id = cls_name + "." + s_l[1]
                            setattr(obj_dict[obj_id], s_l[2], s_l[3])
                            storage.save()
                    else:
                        print("** unknown syntax **")

            except IndexError:
                print("** attribute value missing **")
        else:
            print("** unknown syntax **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
