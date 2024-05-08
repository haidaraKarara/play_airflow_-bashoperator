FROM quay.io/astronomer/astro-runtime:11.3.0

USER astro

RUN chmod +x /usr/local/airflow/include/scripts/simple_bash_script.sh
RUN chmod +x /usr/local/airflow/include/scripts/my_js_script.js
RUN chmod +x /usr/local/airflow/include/scripts/my_r_script.r
