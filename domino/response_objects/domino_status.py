import datetime

class DominoStatusResponse:
    def __init__(self, domino_response):
        self._raw_response = domino_response
        self.domino_status = DominoStatus(domino_response)
        self.status_types = [
            "Scheduled"
            "Queued",
            "Preparing",
            "Running",
            "Finishing"
            "Stopped",
            "Failed",
            "Succeeded"
        ]
        self.status_types_done = [
            "Stopped",
            "Failed",
            "Succeeded"
        ]

    def is_done(self):
        return self.domino_status.status in self.status_types_done

class DominoStatus:
    def __init__(self, response_json):
        self.id = response_json["id"]
        self.project_id = response_json["projectId"]
        self.number = response_json["number"]
        self.starting_user_id = response_json["startingUserId"]
        self.queued_utc = self._parse_utc_timestamp_optional(response_json["queued"])
        self.started_utc = self._parse_utc_timestamp_optional(response_json["started"])
        self.completed_utc = self._parse_utc_timestamp_optional(response_json["completed"])
        self.status = response_json["status"]
        self.commit_id = response_json["commitId"]
        self.executor = response_json["executor"]
        self.output_commit_id = response_json["outputCommitId"]
        self.title = response_json["title"]
        self.is_archived = response_json["isArchived"]
        self.post_processed_timestamp_utc = self._parse_utc_timestamp_optional(response_json["postProcessedTimestamp"])
        self.diagnostic_statistics = response_json["diagnosticStatistics"]
        self.is_completed = response_json["isCompleted"]

    def _parse_utc_timestamp_optional(self, timestamp_microsecond):
        if timestamp_microsecond is None:
            return None
        return datetime.datetime.utcfromtimestamp(timestamp_microsecond / 1000.0)
