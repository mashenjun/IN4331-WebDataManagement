
\version "2.18.2"
% automatically converted by musicxml2ly from lg-5367080.xml

\header {
    encodingsoftware = "MuseScore 2.0.1"
    source = "http://musescore.com/score/859806"
    encodingdate = "2015-05-11"
    composer = "Johann Sebastian Bach (1685-1750)"
    title = Air
    }

#(set-global-staff-size 20.0750126457)
\paper {
    paper-width = 21.01\cm
    paper-height = 29.69\cm
    top-margin = 1.0\cm
    bottom-margin = 2.0\cm
    left-margin = 1.0\cm
    right-margin = 1.0\cm
    }
\layout {
    \context { \Score
        autoBeaming = ##f
        }
    }
PartPOneVoiceOne =  \relative b' {
    \repeat volta 2 {
        \clef "treble" \key g \major \time 4/4 | % 1
        \tempo 4=100 b1 ~ | % 2
        b1 ~ | % 3
        b4 e8 [ c8 ] a8 [ g8 fis8 g8 ] | % 4
        fis4. e8 d2 | % 5
        d'1 ~ | % 6
        d8 [ b8 f8 e8 ] a8 [ gis8 d'8 c8 ] | % 7
        c1 ~ | % 8
        c8 [ a8 e8 d8 ] g8 [ fis8 c'8 b8 ] \break | % 9
        b2. cis8 [ d8 ] | \barNumberCheck #10
        g,4 g16 [ a16 b8 ~ ] b8 [ a8 a8 g8 ] }
    \alternative { {
            | % 11
            fis8 [ e8 ] e16 [ fis16 g8 ~ ] g4 fis8 [ e8 ] | % 12
            d1 }
        {
            | % 13
            fis8 [ e8 ] e16 [ fis16 g8 ~ ] g4 fis8 [ e8 ] | % 14
            d1 }
        } | % 15
    fis2 ~ fis8 [ g16 fis16 ] e16 [ fis16 d8 ] \break | % 16
    d'2. f,4 | % 17
    e4 e'4 ~ e8 [ d8 c8 b8 ] | % 18
    c2 ~ c16 [ b16 a16 g16 ] fis8 [ e8 ] | % 19
    dis8 [ e8 ] fis4 ~ fis8 [ g8 ] a4 ~ | \barNumberCheck #20
    a8 [ b8 ] c2 b4 | % 21
    a8 [ g8 fis8 e8 ] fis8 [ g16 a16 ] g8 [ fis8 ] | % 22
    fis4 e2. \break | % 23
    g2 ~ g8 [ b8 a8 g8 ] | % 24
    e'2. d8 [ cis8 ] | % 25
    b16 [ a16 d8 ] d,4 e4. fis16 [ g16 ] | % 26
    fis4. e8 d2 | % 27
    g2. b8 [ a8 ] | % 28
    a2. c8 [ b8 ] | % 29
    b2. d8 [ c8 ] | \barNumberCheck #30
    c1 \break | % 31
    d,2 ~ d8 [ fis8 a8 c8 ] | % 32
    c8 [ a8 ] b2 ~ b8 [ c16 d16 ] | % 33
    g,2 ~ g8 [ b8 d8 f8 ] | % 34
    e2. g,4 | % 35
    fis8 [ a8 ] c2 e,4 | % 36
    d4 a'16 [ b16 c8 ~ ] c8 b4 a8 | % 37
    g16 [ fis16 e8 ] e8 [ fis8 ] fis4. g8 \break | % 38
    g1 \bar "|."
    }


% The score definition
\score {
    <<
        \new Staff <<
            \set Staff.instrumentName = "C Trompete"
            \set Staff.shortInstrumentName = "C Tpt."
            \context Staff << 
                \context Voice = "PartPOneVoiceOne" { \PartPOneVoiceOne }
                >>
            >>
        
        >>
    \layout {}
    % To create MIDI output, uncomment the following line:
    %  \midi {}
    }

