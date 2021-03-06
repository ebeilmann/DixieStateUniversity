#ifndef _ARTEMIS_H_
#define _ARTEMIS_H_

//#include "eebaction.h"
//#include "eebmodel.h"
#include <ai_wumpus.h>
#include <ai_pl.h>
#include <list>


namespace eeba
{
	enum Moves { NORTH=0, SOUTH=1, EAST=2, WEST=3, FORWARD=4,TURN_RIGHT=5,TURN_LEFT=6,GRAB=7,SHOOT=8,QUIT=9,ERROR};
	
	class Artemis : public ai::Agent::AgentProgram
	{
	public:
		Artemis();
		~Artemis();
		virtual ai::Agent::Action * Program(const ai::Agent::Percept * percept);
		
	protected:
		bool rules();
		bool goalsearch();
		bool parsepercepts(const ai::Agent::Percept *percept);
		//questions
		bool AskVisited();
		//bool AskNextSafe();
		
		bool AskNextPit();
		bool AskNextWumpus();
		bool AskNextWall();
		bool AskShoot();
		bool AskGlitter();
		bool AskSmellyStart();
		bool AskBreezyStart();
		bool ShotResults();
		bool AskVisited(int a,int b);
		bool AskNextVisited();
		bool AskNothing();
		bool AskLocalNothing();
		
		bool ChangeDirection(int goal);
		/* Things I know */
		ai::PL::KnowledgeBase eeb;
		/* my location */
		int x;
		int y;
		int dir;
		bool arrow;
		bool golden;
		bool wumpus;
		
		std::list<Moves>actqueue;
	private:
	};
}

#endif /* _ARTEMIS_H_ */
