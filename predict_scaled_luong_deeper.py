import os
FLAG = 'y'

while FLAG == 'y':
  origin_sentence = input('please enter the sentence you want to translate:\n')
  origin_file = open('./input.en', 'w')
  origin_file.write(origin_sentence)
  origin_file.close()

  #subprocess.call(['./translate.sh'])
  os.system('python -m nmt.nmt \
    --src=en --tgt=zh \
    --ckpt=./nmt_attention_model_scaled_luong_50w_deeper/translate.ckpt-210000\
    --out_dir=./nmt_attention_model_scaled_luong_50w_deeper \
    --vocab_prefix=./nmt_attention_model_scaled_luong_50w_deeper/vocab \
    --inference_input_file=./input.en \
    --inference_output_file=./output.zh \
   '
)
  result_file = open('./output.zh', 'r')
  result_sentence = result_file.read().replace(" ","")
  print('The translated sentence is:\n%s\n' % result_sentence)

  FLAG = input('Would you like to try another sentence? y/n\n').lower()

