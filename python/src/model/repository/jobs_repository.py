from src.model.repository import *

class jobs_repository(repository):
    """
    職業マスタテーブルのリポジトリクラス
    """
    def __init__(self, jobs_entity):
        super().__init__(jobs_entity)
    def find_all_order_by_job_other_last(self, columns, where = '', params = {}, order_by = ''):
        """
        職業マスタテーブルのデータを全て取得する（その他は末尾にする）
        """
        jobs_all_data = super().find_all(
            columns,
            where,
            params,
            order_by
        )
        job_other_dict = {}
        jobs = []
        for index, row in enumerate(jobs_all_data):
            # その他は末尾にする
            if 0 == index:
                job_other_dict = {'id': row.job_id, 'name': row.job_name}
            else:
                jobs_dict = {'id': row.job_id, 'name': row.job_name}
                jobs.append(jobs_dict)
        jobs.append(job_other_dict)
        return jobs
