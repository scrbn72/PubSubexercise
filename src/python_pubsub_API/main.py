from lib.pubsubapi import PubSubAPI

def main():
    project_id = "training-gcp-309207"
    topic_id = "ex_lombardica-topic"
    subscription_id = "ex_lombardica-subscription"
    message = "Primo messaggio PubSub del mio progetto"

    pubsub_api = PubSubAPI(project_id)

    # Create topic
    pubsub_api.create_topic(topic_id)

    # Create subscription
    pubsub_api.create_subscription(topic_id, subscription_id)

    # Publish message
    pubsub_api.publish_message(topic_id, message)

if __name__ == "__main__":
    main()
