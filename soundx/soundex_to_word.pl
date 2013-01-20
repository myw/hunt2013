use strict;
use warnings;
use Text::Soundex;

open FILE, "<", "dict1";
my @dict;

SLURPFILE: {
	local $/ = undef;
	push @dict, split(/\W+/, <FILE>);
}

my $inputsoundex = $ARGV[0];

if ($inputsoundex) {
	foreach my $word (@dict) {
		print "$word\n" if soundex($word) eq $inputsoundex;
	}
}

