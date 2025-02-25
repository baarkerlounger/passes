# pkpass_row.py
#
# Copyright 2022 Pablo Sánchez Rodríguez
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from gi.repository import Gdk, Gtk

from .colored_box import ColoredBox
from .pkpass_row_header import PassRowHeader


@Gtk.Template(resource_path='/me/sanchezrodriguez/passes/pkpass_row.ui')
class PassRow(Gtk.ListBoxRow):

    __gtype_name__ = 'PassRow'

    colored_box = Gtk.Template.Child()

    icon = Gtk.Template.Child()
    name = Gtk.Template.Child()

    def __init__(self, a_pass):
        super().__init__()
        self.__pass = a_pass

        try:
            background_color = self.__pass.background_color().as_tuple()
        except:
            background_color = (0,0,0)

        icon_data = self.__pass.icon().read_pixel_bytes().get_data()
        if not self.__pass.icon().get_has_alpha() or icon_data[3] > 0:
            background_color = icon_data[0:3]

        self.colored_box.color(*background_color)
        self.icon.set_from_pixbuf(a_pass.icon())
        self.name.set_text(a_pass.description())

    def data(self):
        return self.__pass

    def hide_header(self):
        self.set_header(None)

    def show_header(self):
        header = PassRowHeader(self.__pass.style())
        self.set_header(header)

    def style(self):
        return self.__pass.style()
