import preprocess_unbong as pun
import preprocess_leaf as ple
import preprocess_stem as pst
import preprocess_seed as pse
import preprocess_timedata as pti
import preprocess_data as pda

# 1. preprocess_unbong => 생육조사데이터 엑셀파일을 CSV형식 변환 후 저장
pun.save_unbong()

# # 2. preprocess_leaf => 개화기 이후 5.10~5.31 leaf의 건물중, 생체중, 수분함량
# ple.save_leaf()
#
# # 3. preprocess_stem => 개화기 이후 5.10~5.31 stem의 건물중, 생체중, 수분함량
# pst.save_stem()

# 4. preprocess_seed => 개화기 이후 5.10~5.31 seed의 건물중, 생체중, 수분함량
pse.save_seed()

# 5. preprocess_timedata => 개화기 이후 5.10~5.31 leaf, stem, seed의 데이터를 합쳐 시계열화
pti.save_data_to_time()

# 6. preprocess_data => 개화기 이후 5.10~5.31 leaf, stem, seed의 데이터를 세로로 합치기
pda.save_data()