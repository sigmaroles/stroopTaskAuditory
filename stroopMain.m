%InitializaPsychSound();

%phandle = PsychPortAudio('Open', 0, 1, 0, 44100, 2);
%PsychPortAudio('Volume', pahandleInternal, params.extNoiseLevel);

f = fopen('experiment_cond_filenames.csv');
g = textscan(f, '%s', 'Delimiter', '\n');
g1 = g{1};
data = g1(2:end);
fclose(f);