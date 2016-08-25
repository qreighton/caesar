#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2


def user_input_is_valid(cl_args):
    if len(cl_args) < 2:
        return False
    if cl_args[1].isdigit() == False:
        return False
    return True

def encrypt(text,rot):
    text2 = list(text)
    c = ""
    for i in text2:
        b = rotate_character(i,rot)
        c = c + b
    return c
def alphabet_position(letter):
    count = ord(letter)
    if ord(letter) < 97:
        count = count+32
    count = count = count - 97
    return count

def rotate_character(char,rot):
    rot = int(rot)
    if char.isalpha():
        a = alphabet_position(char)
        a = a + rot
        a = a % 26
        if ord(char) > 90:
            b = chr(a + 97)
        else:
            b = chr(a + 65)
        return b
    return char
# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Caesar</title>
</head>
<body>
    <h1>Caesar</h1>
"""
rotation_header = "<h3>Enter the rotation for message</h3>"
message_header = "<h3>Enter your message</h3>"
message_form = """
<form action="/change" method="post">
    <label>
        <input type="text" name="rotation" value = "%(orot)s"/>
    </label>
    <br>
    <h3>Enter your message</h3>
    <br>
    <textarea name="message" style = "height:100px;width:400px;"> %(crypt)s
    </textarea>
    <br>
    <input type="submit" value="submit"/>

</form>
"""
# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""

class Codex(webapp2.RequestHandler):

    def get(self):
        crypt =""
        orot =""
        response = page_header + rotation_header + message_form + page_footer
        self.response.write(response % {"crypt":crypt,"orot":orot})


class cypher(webapp2.RequestHandler):

    def post(self):
        rotate = self.request.get("rotation")
        text= self.request.get("message")
        crypt = encrypt(text,rotate)
        orot = rotate
        response = page_header + rotation_header +message_form + page_footer
        self.response.out.write(response % {"crypt":crypt,"orot":orot})

app = webapp2.WSGIApplication([
                          ('/', Codex),
                          ('/change', cypher)
], debug=True)
