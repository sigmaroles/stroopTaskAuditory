res_dir = './resources'
fname_f = 'words_f'
fname_m = 'words_m'

"""
basic goal: read the word lists and file names, and generate a csv file
the csv specifies exact trial sequence

conditions:
1 : ANC (on/off)
2 : congruent (yes/no) --> yes = male word by male speaker, no otherwise etc.
3 : task (voice/word) --> whether participant should report on word gender or voice gender


Note: all words have two files, 
m_{word}.wav 
and 
f_{word}.wav 
generate filenames accordingly. display warning if a paricular file is calculated (from word list) but not found in directory

csv header:
cond_congruent, filename

sample rows of csv: 
yes, m_masculine.wav
no, m_woman.wav

etc.

"""

if __name__=='__main__':
    
    # read the words of both genders
    with open(res_dir + '/' + fname_f, 'r') as fhandle1:
        f_words = fhandle1.read().split('\n')
        
    with open(res_dir + '/' + fname_m, 'r') as fhandle2:
        m_words = fhandle2.read().split('\n')


    allwords = {'m': m_words, 'f': f_words}


    header = "cond_congruent, filename"
    
    fout = open('experiment_cond_filenames.csv', 'w')
    fout.write(header+"\n")

    for cond_congruent in ["yes", "no"]:
        # row = cond_ANC + "," + cond_task + "," + cond_congruent + ","
        if cond_congruent == "yes":
            # prefix 'm' before elements of allwords['m'] and similar for 'f'
            filenames = ['m_'+x+'.wav' for x in allwords['m']] + ['f_'+x+'.wav' for x in allwords['f']]
        else:
            filenames = ['m_'+x+'.wav' for x in allwords['f']] + ['f_'+x+'.wav' for x in allwords['m']]

        for fn in filenames:
            fout.write(cond_congruent + ',' + fn + '\n')     

                
    fout.close()                
        
    