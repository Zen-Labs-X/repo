- fix: some display issues, pr  from @GOSENGWONG :

    The author line in module_hero_currently and the Cover Deck description
    strip both overflowed their box. Both now let TextBoxWidget do the clipping
    via height + height_overflow_show_ellipsis instead of hand-rolled measurement.