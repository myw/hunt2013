use Text::Soundex;

open FILE, "<", "dict1";
my @dict;

{local $/ = undef;
 push @dict, split(/\W+/, <FILE>);
}

foreach $word(@dict)
{
    $lookup{soundex($word)}.="|$word";
}

while($line = <>)
{
    print $lookup{soundex($line)}."\n";
}
