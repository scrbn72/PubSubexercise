from google.cloud import pubsub_v1

class PubSubAPI:
    def __init__(self, project_id):
        self.project_id = project_id
        self.publisher = pubsub_v1.PublisherClient()
        self.subscriber = pubsub_v1.SubscriberClient()

    def create_topic(self, topic_id):
        topic_path = self.publisher.topic_path(self.project_id, topic_id)
        topic = self.publisher.create_topic(request={"name": topic_path})
        print(f"Created topic: {topic.name}")
        return topic

    def create_subscription(self, topic_id, subscription_id):
        topic_path = self.publisher.topic_path(self.project_id, topic_id)
        subscription_path = self.subscriber.subscription_path(self.project_id, subscription_id)
        subscription = self.subscriber.create_subscription(request={"name": subscription_path, "topic": topic_path})
        print(f"Created subscription: {subscription.name}")
        return subscription

    def publish_message(self, topic_id, message):
        topic_path = self.publisher.topic_path(self.project_id, topic_id)
        future = self.publisher.publish(topic_path, message.encode("utf-8"))
        print(f"Published message ID: {future.result()}")
