#import <Foundation/NSObject.h>
#import <stdio.h>
 
@interface Person : NSObject
  - (void) sayHello;
@end
 
@implementation Person
 
- (void) sayHello{
  printf("Hello Objective-C World.\n");
}
 
@end
 
int main(void) {
  id person = [Person alloc];
  [person sayHello];
 
  return 0;
}
