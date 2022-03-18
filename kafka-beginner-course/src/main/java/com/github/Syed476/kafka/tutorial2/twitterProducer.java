package com.github.Syed476.kafka.tutorial2;

import com.google.common.collect.Lists;
import com.twitter.hbc.ClientBuilder;
import com.twitter.hbc.core.Client;
import com.twitter.hbc.core.Constants;
import com.twitter.hbc.core.Hosts;
import com.twitter.hbc.core.HttpHosts;
import com.twitter.hbc.core.endpoint.StatusesFilterEndpoint;
import com.twitter.hbc.core.processor.StringDelimitedProcessor;
import com.twitter.hbc.httpclient.auth.Authentication;
import com.twitter.hbc.httpclient.auth.OAuth1;
import org.apache.kafka.clients.producer.*;
import org.apache.kafka.common.serialization.StringSerializer;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.List;
import java.util.Properties;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.LinkedBlockingQueue;
import java.util.concurrent.TimeUnit;

public class twitterProducer {
    Logger logger = LoggerFactory.getLogger(twitterProducer.class.getName());
    public twitterProducer(){}
    public static void main(String[] args) {
        new twitterProducer().run();
    }
    public void run(){
        /** Set up your blocking queues: Be sure to size these properly based on expected TPS of your stream */
        BlockingQueue<String> msgQueue = new LinkedBlockingQueue<String>(100);
        // Attempts to establish a connection.
        Client client = createTwitterClient(msgQueue);
        client.connect();

        KafkaProducer<String,String> producer = createKafkaProducer();
        // on a different thread, or multiple different threads....
        Runtime.getRuntime().addShutdownHook(new Thread(() ->{
           logger.info("Stopping application..");
           logger.info("Shutting down twitter client ..");
           client.stop();
           producer.close();
           logger.info("done..");
        }));
        while (!client.isDone()) {
            String msg=null;
            try {
                 msg = msgQueue.poll(5, TimeUnit.SECONDS);
            } catch (InterruptedException e){
                e.printStackTrace();
                client.stop();
            }
            if (msg !=null){
                logger.info(msg);
                producer.send(new ProducerRecord<>("twitter_tweets",null,msg),new Callback(){
                    @Override
                    public void onCompletion(RecordMetadata recordMetadata, Exception e){
                        if (e!=null){
                            logger.error("Something happened!",e);
                        }
                    }
                });
            }
        }

        logger.info("End of application");
    }
    String ConsumerKey="96N5sVIntCJOH1BFh20g1nZdm";
    String ConsumerSecret="VFt3LZB1EjbrWOMrEOdmyeizbL7TCaHWyoiCFspSZ0m9kgZKe5";
    String token="1471145267999170564-m3hhXTq1iIeG42BkFdWDTBtfpt8xts";
    String secret="ac9GiZrzdNeFtZnqowvJSGSYYG7wqgjRWOsRGFmE0EuJU";
    List<String> terms = Lists.newArrayList("kafka");

    public Client createTwitterClient(BlockingQueue<String> msgQueue){


        /** Declare the host you want to connect to, the endpoint, and authentication (basic auth or oauth) */
        Hosts hosebirdHosts = new HttpHosts(Constants.STREAM_HOST);
        StatusesFilterEndpoint hosebirdEndpoint = new StatusesFilterEndpoint();
        // Optional: set up some followings and track terms


        hosebirdEndpoint.trackTerms(terms);

        // These secrets should be read from a config file
        Authentication hosebirdAuth = new OAuth1(ConsumerKey,ConsumerSecret,token,secret);

        ClientBuilder builder = new ClientBuilder()
                .name("Hosebird-Client-01")                              // optional: mainly for the logs
                .hosts(hosebirdHosts)
                .authentication(hosebirdAuth)
                .endpoint(hosebirdEndpoint)
                .processor(new StringDelimitedProcessor(msgQueue));
        // optional: use this if you want to process client events

        Client hosebirdClient = builder.build();
        return hosebirdClient;
    }
    public KafkaProducer <String,String> createKafkaProducer (){
        String bootstrapServers = "127.0.0.1:9092";
        //System.out.println("hello world");
        Properties properties=new Properties();
        properties.setProperty(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG,bootstrapServers);
        properties.setProperty(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
        properties.setProperty(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG,StringSerializer.class.getName());

        KafkaProducer<String,String> producer= new KafkaProducer<String, String>(properties);
        return producer;
    }
}
