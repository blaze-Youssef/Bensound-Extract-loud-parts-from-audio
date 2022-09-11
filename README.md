
# Bensound-Extract-loud-parts-from-audio
Simple module to extract loud parts in a audio file.
## Usage

    from  benSound  import  get_loudest_parts_onedir, get_loudest_parts_onefile
**`get_loudest_parts_onefile`** will arrange all parts in one long file, It can get this arguments:

 1. song -> Song file.
 2. x -> Default is 0.1, **this very important**: You need to tweak this value to get your desired results.
 3. outputfile -> Final output path.
 4. chunk_length_ms -> Default is 5000 ms, The module will slice the audio file to slices of this duration to analyze.
 
 **`get_loudest_parts_onedir`** will write all parts to one directory, It can get this arguments:
 
 1. song -> Song file.
 2. x -> Default is 0.1, **this very important**: You need to tweak this value to get your desired results.
 3. outputdir -> Final output directory of audio segments.
 4. chunk_length_ms -> Default is 5000 ms, The module will slice the audio file to slices of this duration to analyze.
