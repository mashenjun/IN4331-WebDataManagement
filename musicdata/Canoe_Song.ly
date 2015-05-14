
\version "2.18.2"
% automatically converted by musicxml2ly from Canoe_Song.xml

\header {
    encodingsoftware = "MuseScore 1.2"
    encodingdate = "2012-08-16"
    }

\layout {
    \context { \Score
        skipBars = ##t
        autoBeaming = ##f
        }
    }
PartPOneVoiceOne =  \relative a' {
    \clef "treble" \key f \major \numericTimeSignature\time 4/4 R1*4
    \repeat volta 2 {
        | % 5
        a8 a4 g8 f8 [ d8 ] d4 | % 6
        f8 f4 g8 a4 d4 | % 7
        a8 a4 g8 f8 [ d8 ] d4 | % 8
        d8 d4 c8 d4 r4 }
    }

PartPOneVoiceOneLyricsOne =  \lyricmode { My pad "dle's" keen "bright,"
    Flash ing with sil "ver." Fol low the wild "flight," "Dip," dip and
    "swing." }
PartPOneVoiceOneLyricsTwo =  \lyricmode { "Dip," dip and swing "paddle,"
    Flash ing with sil "ver." Fol low the wild "flight," "Dip," dip and
    "swing." }
PartPTwoVoiceOne =  \relative a'' {
    \clef "treble^8" \key f \major \numericTimeSignature\time 4/4 <a a'>4
    r4 r2 | % 2
    r2 r4 <a a'>4 | % 3
    <a a'>4 r4 r2 | % 4
    r2 r4 <a a'>4 \repeat volta 2 {
        | % 5
        <a a'>4 r4 r2 | % 6
        r2 r4 <a a'>4 | % 7
        <a a'>4 r4 r2 | % 8
        r2 r8 a8 a'4 }
    }

PartPThreeVoiceOne =  \relative b' {
    \clef "percussion" \stopStaff \override Staff.StaffSymbol
    #'line-count = #1 \startStaff \key c \major
    \numericTimeSignature\time 4/4 r2 b8 [ b8 b8 b8 ] | % 2
    r2 b8 [ b8 ] b4 | % 3
    r2 b8 [ b8 b8 b8 ] | % 4
    r2 b8 [ b8 ] b4 \repeat volta 2 {
        | % 5
        r2 b8 [ b8 b8 b8 ] | % 6
        r2 b8 [ b8 ] b4 | % 7
        r2 b8 [ b8 b8 b8 ] | % 8
        r2 b8 [ b8 ] b4 }
    }

PartPFourVoiceOne =  \relative d' {
    \clef "treble" \key f \major \numericTimeSignature\time 4/4 <d a'>2
    <d a'>2 | % 2
    <d a'>4 <d a'>4 <d a'>2 | % 3
    <d a'>2 <d a'>2 | % 4
    <d a'>4 <d a'>4 <d a'>2 \repeat volta 2 {
        | % 5
        <d a'>2 <d a'>2 | % 6
        <d a'>4 <d a'>4 <d a'>2 | % 7
        <d a'>2 <d a'>2 | % 8
        <d a'>4 <d a'>4 <d a'>2 }
    }


% The score definition
\score {
    <<
        \new Staff <<
            \set Staff.instrumentName = "Soprano"
            \set Staff.shortInstrumentName = "S."
            \context Staff << 
                \context Voice = "PartPOneVoiceOne" { \PartPOneVoiceOne }
                \new Lyrics \lyricsto "PartPOneVoiceOne" \PartPOneVoiceOneLyricsOne
                \new Lyrics \lyricsto "PartPOneVoiceOne" \PartPOneVoiceOneLyricsTwo
                >>
            >>
        \new Staff <<
            \set Staff.instrumentName = "Orff Alto Glockenspiel"
            \set Staff.shortInstrumentName = "O. A. Glk."
            \context Staff << 
                \context Voice = "PartPTwoVoiceOne" { \PartPTwoVoiceOne }
                >>
            >>
        \new RhythmicStaff <<
            \set RhythmicStaff.instrumentName = "Tambourine"
            \set RhythmicStaff.shortInstrumentName = "Tamb."
            \context RhythmicStaff << 
                \context Voice = "PartPThreeVoiceOne" { \PartPThreeVoiceOne }
                >>
            >>
        \new Staff <<
            \set Staff.instrumentName = "Orff Alto Xylophone"
            \set Staff.shortInstrumentName = "O. A. Xyl."
            \context Staff << 
                \context Voice = "PartPFourVoiceOne" { \PartPFourVoiceOne }
                >>
            >>
        
        >>
    \layout {}
    \midi {}
    }

