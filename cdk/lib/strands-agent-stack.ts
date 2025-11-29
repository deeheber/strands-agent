import { Stack, StackProps } from 'aws-cdk-lib'
import { Construct } from 'constructs'
// import { Queue } from 'aws-cdk-lib/aws-sqs';
// import { Duration } from 'aws-cdk-lib';

export class StrandsAgentStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props)

    // The code that defines your stack goes here

    // example resource
    // const queue = new Queue(this, 'StrandsAgentQueue', {
    //   visibilityTimeout: Duration.seconds(300)
    // });
  }
}
