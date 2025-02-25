hadoop jar /home/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
-D mapred.reduce.tasks=5 \
-files mapper.py,combiner.py,reducer.py,years.txt,genres.txt \
-mapper mapper.py \
-combiner combiner.py \
-reducer reducer.py \
-input /user/xyz123/assignment/ratings.txt \
-output /user/xyz123/assignment/results