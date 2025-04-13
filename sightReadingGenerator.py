# Sight Reading Generator

import abjad
string = "g'4 a' b' d'' c'' c'' e'' d'' d'' g'' fs'' g'' d'' b' g' a'4"
voice_1 = abjad.Voice(string, name="Voice_1")
staff_1 = abjad.Staff([voice_1], name="Staff_1")
abjad.show(staff_1)