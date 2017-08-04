# ovasum
A very simple script to check if ova files are intact without needing to deploy them.
The need for this arose when a drive containing ova files was overwritten, and there existed no tool to check the recovered ova files.
An ova file is simply a tar file, it contains mf, ovf and vmdk files.
The mf file contains the names and hashes of the ovf and vmdk files.

ovasum was designed to not have to unpack the files from the ova, and to stream the files when checking, to make a mess free and minimal RAM script.

This script is by no means complete or functional in every scenario, it was a quick hack that worked on the sample of ova files given, it will not work on all ova files until the mf parser is rewritten.
I also haven't studied the ova standard (if it is a standard) so I do not know if this takes into account all aspects of an ova when verifying it.

TODO:
- Refactor to make it less crap
- Add proper exception handling
- ~~Rewrite the mf parser to be able to reliably parse any valid mf file~~
- Create a nice data structure for the parsed manifest
- Add timestamps to console output
- Add progress bars for checking
- Add colours to the pass and fail messages
- Add summary for showing number of files passed and failed
- Add ability to make a log file, specify with flag
