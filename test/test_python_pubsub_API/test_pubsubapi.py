import unittest
from unittest.mock import patch, MagicMock
from google.cloud import pubsub_v1
from src.python_pubsub_API.lib.pubsubapi import PubSubAPI

class TestPubSubAPI(unittest.TestCase):

    @patch('google.cloud.pubsub_v1.PublisherClient.create_topic')
    def test_create_topic(self, mock_create_topic):
        # Configura il mock per create_topic
        mock_topic = MagicMock()
        mock_topic.name = "projects/test-project/topics/test-topic"
        mock_create_topic.return_value = mock_topic

        project_id = "test-project"
        topic_id = "test-topic"
        pubsub_api = PubSubAPI(project_id)
        topic = pubsub_api.create_topic(topic_id)

        mock_create_topic.assert_called_once_with(request={"name": f"projects/{project_id}/topics/{topic_id}"})
        self.assertEqual(topic.name, f"projects/{project_id}/topics/{topic_id}")

    @patch('google.cloud.pubsub_v1.SubscriberClient.create_subscription')
    def test_create_subscription(self, mock_create_subscription):
        # Configura il mock per create_subscription
        mock_subscription = MagicMock()
        mock_subscription.name = "projects/test-project/subscriptions/test-subscription"
        mock_create_subscription.return_value = mock_subscription

        project_id = "test-project"
        topic_id = "test-topic"
        subscription_id = "test-subscription"
        pubsub_api = PubSubAPI(project_id)
        subscription = pubsub_api.create_subscription(topic_id, subscription_id)

        mock_create_subscription.assert_called_once_with(request={
            "name": f"projects/{project_id}/subscriptions/{subscription_id}",
            "topic": f"projects/{project_id}/topics/{topic_id}"
        })
        self.assertEqual(subscription.name, f"projects/{project_id}/subscriptions/{subscription_id}")

    @patch('google.cloud.pubsub_v1.PublisherClient.publish')
    def test_publish_message(self, mock_publish):
        # Configura il mock per publish
        mock_future = MagicMock()
        mock_future.result.return_value = "mock_message_id"
        mock_publish.return_value = mock_future

        project_id = "test-project"
        topic_id = "test-topic"
        message = "Hello, world!"
        pubsub_api = PubSubAPI(project_id)
        pubsub_api.publish_message(topic_id, message)

        mock_publish.assert_called_once_with(f"projects/{project_id}/topics/{topic_id}", message.encode("utf-8"))
        self.assertEqual(mock_future.result(), "mock_message_id")

if __name__ == '__main__':
    unittest.main()
